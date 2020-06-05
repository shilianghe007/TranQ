<template>
<div>
  <div class="container-fluid">
    <div class="row">
    <div class="col-md-6" align="center">
      <canvas id="myCanvas" width="500" height="500" style="border:1px solid #d7caee;margin-top: 20px;">
      </canvas>
    </div>
    <div class="col-md-6" style="margin-top: 20px">
      <h2>
        迭代结果：
      </h2>
      <p>
        迭代进度：{{iter - 1}}/200
      </p>
      <p>
        路线总长度：{{sum_length}}
      </p>
      <p>
        满载率：{{manzai}}
      </p>
      <p>
        整体适应度：{{fit}}
      </p>
      <p>
        使用车辆数：{{this.routes.length}}
      </p>
      <p
        v-for="(singleroute, index) in routes"
        :key="index">
        路线{{index}}：{{singleroute}}
      </p>
      <p>
        <a class="btn" href="#">View details »</a>
      </p>
    </div>
    </div>
    <div class="row" id = "iterationsPre" style="margin-top: 20px">
    <div class="col-md-12" align="center">
      <h3>迭代中配送路径长度变化折线图</h3>
      <h5>最大值:{{maxlen}}   最小值:{{minlen}}</h5>
      <canvas id="myCanvas3" width="1200" height="300" style="border:1px solid #d7caee;margin-top: 20px;margin-bottom: 40px;">
      </canvas>
    </div>
    </div>
    <div class="row" id = "bestAns">
    <div class="col-md-6" align="center">
      <canvas id="myCanvas2" width="500" height="500" style="border:1px solid #d7caee;margin-top: 20px;">
      </canvas>
    </div>
    <div class="col-md-6" style="margin-top: 20px">
      <h2>
        最终结果：
      </h2>
      <p>
        路线总长度：{{sum_length2}}
      </p>
      <p>
        满载率：{{manzai2}}
      </p>
      <p>
        使用车辆数：{{this.routes2.length}}
      </p>
      <p
        v-for="(singleroute, index) in routes2"
        :key="index">
        路线{{index}}：{{singleroute}}
      </p>
      <p>
        <button @click="downloadResult()">导出结果</button>
      </p>
    </div>
    </div>
  </div>
</div>
</template>

<script>
/* eslint-disable camelcase */

export default {
  name: 'PresentationIndex',
  data () {
    return {
      msg: {},
      token: '',
      iter: 1,
      iter_result: {},
      sum_length: 0,
      manzai: 0,
      routes: [],
      update: false,
      fit: 0,
      iter_result2: {},
      sum_length2: '迭代还未结束，请稍等',
      manzai2: '迭代还未结束，请稍等',
      routes2: [],
      maxlen: Infinity,
      minlen: 0
    }
  },
  mounted: function () {
    // 每次进入界面时，先清除之前的所有定时器，然后启动新的定时器
    // this.msg = (JSON.parse(this.$store.state.location)).location[0]
    // 先让最终结果隐藏
    document.getElementById('bestAns').style.display = 'none'
    this.$store.state.lengths = ''
    this.msg = this.$store.state.location
    this.token = this.$store.state.token
    // this.token = 'VNYLTZIR71NO22SDZO4LBM92B6UNAFZVPQK8AF951LF1INFIILRIYJHZ54Y6IXS0'
    this.getResult()
    if (this.update === true) {
      this.drawMap()
    }
    clearInterval(this.timer)
    this.timer = null
    this.setTimer()
  },
  beforeDestroy () { // 页面关闭前关闭定时器 （这个才有用）
    clearInterval(this.timer)
    this.timer = null
  },
  methods: {
    getResult () {
      console.log('aaa')
      console.log(this.iter - 1)
      this.$axios
        .get('/get_iterresult', {
          params: {
            token: this.token,
            iter_id: this.iter - 1
          }
        })
        .then(successResponse => {
          console.log(successResponse)
          if (successResponse.data.error_num === 0) {
            this.iter_result = successResponse.data
            this.iter += 1
            // 对接收到的数据进行处理
            var fitFull = successResponse.data.ave_fit
            var i = 0
            var manzai = ''
            var fit = ''
            for (i = 0; i < fitFull.length; i++) {
              if (fitFull.charAt(i) !== '#') {
                fit += fitFull.charAt(i)
              } else {
                i++
                break
              }
            }
            for (; i < fitFull.length; i++) {
              manzai += fitFull.charAt(i)
            }
            console.log(fit)
            this.fit = parseFloat(fit)
            this.manzai = parseFloat(manzai)
            this.sum_length = successResponse.data.best_length
            this.$store.commit('setLength', this.$store.state.lengths + this.sum_length + '#') // 初始化
            this.routes = []
            var routeString = successResponse.data.best_route
            var singleRoute = [] // 记录单条路径中的各点顺序
            var temp = ''
            var num = ''
            for (i = 0; i < routeString.length;) {
              temp = routeString.charAt(i)
              if (temp !== '#') {
                num = num + temp
              } else {
                num = parseInt(num)
                if (num >= this.$store.state.cityNumber) {
                  // 如果已经结束，就将该单条route加入总路线数组中
                  if (singleRoute !== []) {
                    this.routes = this.routes.concat([singleRoute])
                    singleRoute = []
                  }
                } else {
                  // 如果没有结束，就继续加入
                  singleRoute = singleRoute.concat([num])
                }
                num = ''
              }
              i++
            }
            // 避免最后直接结束，所以加上最后的几个数字
            if (num !== '') {
              num = parseInt(num)
              singleRoute = singleRoute.concat([num])
            }
            if (singleRoute !== []) {
              this.routes = this.routes.concat([singleRoute])
              singleRoute = []
            }
            this.routes[0] = this.routes[0].slice(1)
            console.log(this.routes)
            this.update = true
          } else {
            this.update = false
          }
        })
        .catch(failResponse => {
        })
    },
    getResult2 () {
      this.$axios
        .get('/get_iterresult', {
          params: {
            token: this.token,
            iter_id: this.$store.state.iterNum
          }
        })
        .then(successResponse => {
          console.log(successResponse)
          if (successResponse.data.error_num === 0) {
            this.iter_result2 = successResponse.data
            // 对接收到的数据进行处理
            var fitFull = successResponse.data.ave_fit
            var i = 0
            var manzai = ''
            var fit = ''
            for (i = 0; i < fitFull.length; i++) {
              if (fitFull.charAt(i) !== '#') {
                fit += fitFull.charAt(i)
              } else {
                i++
                break
              }
            }
            for (; i < fitFull.length; i++) {
              manzai += fitFull.charAt(i)
            }
            console.log(fit)
            this.manzai2 = parseFloat(manzai)
            this.sum_length2 = successResponse.data.best_length
            this.routes2 = []
            var routeString = successResponse.data.best_route
            var singleRoute = [] // 记录单条路径中的各点顺序
            var temp = ''
            var num = ''
            for (i = 0; i < routeString.length;) {
              temp = routeString.charAt(i)
              if (temp !== '#') {
                num = num + temp
              } else {
                num = parseInt(num)
                if (num >= this.$store.state.cityNumber) {
                  // 如果已经结束，就将该单条route加入总路线数组中
                  if (singleRoute !== []) {
                    this.routes2 = this.routes2.concat([singleRoute])
                    singleRoute = []
                  }
                } else {
                  // 如果没有结束，就继续加入
                  singleRoute = singleRoute.concat([num])
                }
                num = ''
              }
              i++
            }
            // 避免最后直接结束，所以加上最后的几个数字
            if (num !== '') {
              num = parseInt(num)
              singleRoute = singleRoute.concat([num])
            }
            if (singleRoute !== []) {
              this.routes2 = this.routes2.concat([singleRoute])
              singleRoute = []
            }
            this.routes2[0] = this.routes2[0].slice(1)
          }
        })
        .catch(failResponse => {
        })
    },
    drawMap () {
      // 首先获取canvas对象
      var c = document.getElementById('myCanvas')
      var ctx = c.getContext('2d')
      c.height = c.height
      // 对locations进行处理，得到地图边界范围
      var locs = this.$store.state.location.locations
      var centerx = parseFloat(this.$store.state.location.centerx)
      var centery = parseFloat(this.$store.state.location.centery)
      var minx = centerx
      var miny = centery
      var maxx = centerx
      var maxy = centery
      for (var j = 0; j < locs.length; j++) {
        if (minx > parseFloat(locs[j].valuex)) {
          minx = parseFloat(locs[j].valuex)
        }
        if (miny > parseFloat(locs[j].valuey)) {
          miny = parseFloat(locs[j].valuey)
        }
        if (maxx < parseFloat(locs[j].valuex)) {
          maxx = parseFloat(locs[j].valuex)
        }
        if (maxy < parseFloat(locs[j].valuey)) {
          maxy = parseFloat(locs[j].valuey)
        }
      }
      // console.log(minx, miny, maxx, maxy)
      // 开始描点
      var heightCanvas = c.height
      ctx.fillStyle = '#ff36dc'
      ctx.beginPath()
      ctx.arc(heightCanvas * 0.5 + (centerx - (minx + maxx) / 2) * heightCanvas * 0.9 / (maxx - minx), heightCanvas * 0.5 + ((miny + maxy) / 2 - centery) * heightCanvas * 0.9 / (maxy - miny), 5, 0, Math.PI * 2, true)
      ctx.closePath()
      ctx.fill()
      for (j = 0; j < locs.length; j++) {
        ctx.fillStyle = '#ff7c44'
        ctx.beginPath()
        ctx.arc(heightCanvas * 0.5 + (locs[j].valuex - (minx + maxx) / 2) * heightCanvas * 0.9 / (maxx - minx), heightCanvas * 0.5 + ((miny + maxy) / 2 - locs[j].valuey) * heightCanvas * 0.9 / (maxy - miny), 5, 0, Math.PI * 2, true)
        ctx.closePath()
        ctx.fill()
        ctx.font = '20px Arial'
        ctx.fillStyle = '#000000'
        ctx.fillText(j, heightCanvas * 0.5 + (locs[j].valuex - (minx + maxx) / 2) * heightCanvas * 0.9 / (maxx - minx) + 5, heightCanvas * 0.5 + ((miny + maxy) / 2 - locs[j].valuey) * heightCanvas * 0.9 / (maxy - miny))
      }
      // 开始画线
      var lastx, lasty
      var k
      var colors = ['#FF81A3', '#80FF62', '#ffd380', '#efc1ff', '#ff3671', '#ff85d9', '#ff0c0c', '#ffdb0f', '#abfdff', '#5326ff', '#2b82ff', '#a545ff']
      for (j = 0; j < this.routes.length; j++) {
        // 为每一个司机分别画线
        // console.log(colors[j % colors.length])
        lastx = centerx
        lasty = centery
        for (k = 0; k < this.routes[j].length; k++) {
          ctx.beginPath()
          ctx.moveTo(heightCanvas * 0.5 + (lastx - (minx + maxx) / 2) * heightCanvas * 0.9 / (maxx - minx), heightCanvas * 0.5 + ((miny + maxy) / 2 - lasty) * heightCanvas * 0.9 / (maxy - miny))
          ctx.lineTo(heightCanvas * 0.5 + (locs[this.routes[j][k]].valuex - (minx + maxx) / 2) * heightCanvas * 0.9 / (maxx - minx), heightCanvas * 0.5 + ((miny + maxy) / 2 - locs[this.routes[j][k]].valuey) * heightCanvas * 0.9 / (maxy - miny))
          ctx.strokeStyle = colors[j % colors.length]
          ctx.stroke()
          lastx = locs[this.routes[j][k]].valuex
          lasty = locs[this.routes[j][k]].valuey
          // console.log(heightCanvas * 0.5 + (lastx - (minx + maxx) / 2) * heightCanvas * 0.9 / (maxx - minx), heightCanvas * 0.5 + ((miny + maxy) / 2 - lasty) * heightCanvas * 0.9 / (maxy - miny))
          // console.log(this.$store.state.cityNumber)
        }
        ctx.beginPath()
        ctx.moveTo(heightCanvas * 0.5 + (lastx - (minx + maxx) / 2) * heightCanvas * 0.9 / (maxx - minx), heightCanvas * 0.5 + ((miny + maxy) / 2 - lasty) * heightCanvas * 0.9 / (maxy - miny))
        ctx.lineTo(heightCanvas * 0.5 + (centerx - (minx + maxx) / 2) * heightCanvas * 0.9 / (maxx - minx), heightCanvas * 0.5 + ((miny + maxy) / 2 - centery) * heightCanvas * 0.9 / (maxy - miny))
        ctx.strokeStyle = colors[j % colors.length]
        ctx.stroke()
      }
    },
    drawMap3 () {
      // 首先获取canvas对象
      var c = document.getElementById('myCanvas3')
      var ctx = c.getContext('2d')
      c.height = c.height
      // 处理lengths字符串，转换为数组
      let index = 0
      let result = this.$store.state.lengths
      console.log(result)
      let temp_result = []
      let temp_single = ''
      var maxlen = 0
      var minlen = Infinity
      while (index < result.length) {
        if (result.charAt(index) !== '#') {
          temp_single += result.charAt(index)
          index++
        } else {
          let single_num = parseFloat(temp_single)
          if (single_num > maxlen) { maxlen = single_num }
          if (single_num < minlen) { minlen = single_num }
          temp_result = temp_result.concat([single_num])
          temp_single = ''
          index++
        }
      }
      this.maxlen = maxlen
      this.minlen = minlen
      // 画图
      var heightCanvas = c.height
      var widthCanvas = c.width
      ctx.beginPath()
      ctx.moveTo(0, heightCanvas * (maxlen - temp_result[0]) / (maxlen - minlen))
      for (let i = 1; i < temp_result.length; i++) {
        ctx.lineTo(widthCanvas * i / 200, heightCanvas * (maxlen - temp_result[i]) / (maxlen - minlen))
      }
      ctx.strokeStyle = '#7d31ff'
      ctx.stroke()
    },
    drawMap2 () {
      // 首先获取canvas对象
      var c = document.getElementById('myCanvas2')
      var ctx = c.getContext('2d')
      c.height = c.height
      // 对locations进行处理，得到地图边界范围
      var locs = this.$store.state.location.locations
      var centerx = parseFloat(this.$store.state.location.centerx)
      var centery = parseFloat(this.$store.state.location.centery)
      var minx = centerx
      var miny = centery
      var maxx = centerx
      var maxy = centery
      for (var j = 0; j < locs.length; j++) {
        if (minx > parseFloat(locs[j].valuex)) {
          minx = parseFloat(locs[j].valuex)
        }
        if (miny > parseFloat(locs[j].valuey)) {
          miny = parseFloat(locs[j].valuey)
        }
        if (maxx < parseFloat(locs[j].valuex)) {
          maxx = parseFloat(locs[j].valuex)
        }
        if (maxy < parseFloat(locs[j].valuey)) {
          maxy = parseFloat(locs[j].valuey)
        }
      }
      // console.log(minx, miny, maxx, maxy)
      // 开始描点
      var heightCanvas = c.height
      ctx.fillStyle = '#ff36dc'
      ctx.beginPath()
      ctx.arc(heightCanvas * 0.5 + (centerx - (minx + maxx) / 2) * heightCanvas * 0.9 / (maxx - minx), heightCanvas * 0.5 + ((miny + maxy) / 2 - centery) * heightCanvas * 0.9 / (maxy - miny), 5, 0, Math.PI * 2, true)
      ctx.closePath()
      ctx.fill()
      for (j = 0; j < locs.length; j++) {
        ctx.fillStyle = '#ff7c44'
        ctx.beginPath()
        ctx.arc(heightCanvas * 0.5 + (locs[j].valuex - (minx + maxx) / 2) * heightCanvas * 0.9 / (maxx - minx), heightCanvas * 0.5 + ((miny + maxy) / 2 - locs[j].valuey) * heightCanvas * 0.9 / (maxy - miny), 5, 0, Math.PI * 2, true)
        ctx.closePath()
        ctx.fill()
        ctx.font = '20px Arial'
        ctx.fillStyle = '#000000'
        ctx.fillText(j, heightCanvas * 0.5 + (locs[j].valuex - (minx + maxx) / 2) * heightCanvas * 0.9 / (maxx - minx) + 5, heightCanvas * 0.5 + ((miny + maxy) / 2 - locs[j].valuey) * heightCanvas * 0.9 / (maxy - miny))
      }
      // 开始画线
      var lastx, lasty
      var k
      var colors = ['#FF81A3', '#80FF62', '#ffd380', '#efc1ff', '#ff3671', '#ff85d9', '#ff0c0c', '#ffdb0f', '#abfdff', '#5326ff', '#2b82ff', '#a545ff']
      for (j = 0; j < this.routes2.length; j++) {
        // 为每一个司机分别画线
        // console.log(colors[j % colors.length])
        lastx = centerx
        lasty = centery
        for (k = 0; k < this.routes2[j].length; k++) {
          ctx.beginPath()
          ctx.moveTo(heightCanvas * 0.5 + (lastx - (minx + maxx) / 2) * heightCanvas * 0.9 / (maxx - minx), heightCanvas * 0.5 + ((miny + maxy) / 2 - lasty) * heightCanvas * 0.9 / (maxy - miny))
          ctx.lineTo(heightCanvas * 0.5 + (locs[this.routes2[j][k]].valuex - (minx + maxx) / 2) * heightCanvas * 0.9 / (maxx - minx), heightCanvas * 0.5 + ((miny + maxy) / 2 - locs[this.routes2[j][k]].valuey) * heightCanvas * 0.9 / (maxy - miny))
          ctx.strokeStyle = colors[j % colors.length]
          ctx.stroke()
          lastx = locs[this.routes2[j][k]].valuex
          lasty = locs[this.routes2[j][k]].valuey
          // console.log(heightCanvas * 0.5 + (lastx - (minx + maxx) / 2) * heightCanvas * 0.9 / (maxx - minx), heightCanvas * 0.5 + ((miny + maxy) / 2 - lasty) * heightCanvas * 0.9 / (maxy - miny))
          // console.log(this.$store.state.cityNumber)
        }
        ctx.beginPath()
        ctx.moveTo(heightCanvas * 0.5 + (lastx - (minx + maxx) / 2) * heightCanvas * 0.9 / (maxx - minx), heightCanvas * 0.5 + ((miny + maxy) / 2 - lasty) * heightCanvas * 0.9 / (maxy - miny))
        ctx.lineTo(heightCanvas * 0.5 + (centerx - (minx + maxx) / 2) * heightCanvas * 0.9 / (maxx - minx), heightCanvas * 0.5 + ((miny + maxy) / 2 - centery) * heightCanvas * 0.9 / (maxy - miny))
        ctx.strokeStyle = colors[j % colors.length]
        ctx.stroke()
      }
    },
    setTimer () {
      if (this.timer == null) {
        this.timer = setInterval(() => {
          console.log(this.iter)
          // console.log(this.$store.token)
          // this.iter += 1
          if (this.iter <= parseInt(this.$store.state.iterNum)) {
            this.getResult()
            if (this.update === true) {
              this.drawMap()
              this.drawMap3()
            }
          } else {
            document.getElementById('bestAns').style.display = 'inline'
            console.log('画最终图')
            this.getResult2()
            this.drawMap2()
          }
        }, 6000)
      }
    },
    tableToExcel (type) {
      // 要导出的json数据
      const jsonData1 = [
        {
          id: '1',
          x: '3.4',
          y: '2.5',
          need: '3.5'
        },
        {
          id: '2',
          x: '5.4',
          y: '1.4',
          need: '3.6'
        }
      ]
      const jsonData2 = [
        {
          id: '1',
          num: '3',
          weight: '2.6'
        },
        {
          id: '2',
          num: '1',
          weight: '7.6'
        }
      ]
      var jsonData
      var str
      if (type === 0) {
        // 数据
        jsonData = jsonData1
        // 列标题
        str = '<tr><td>序号</td><td>x坐标</td><td>y坐标</td><td>需求量</td></tr>'
      } else {
        // 数据
        jsonData = jsonData2
        // 列标题
        str = '<tr><td>序号</td><td>数量</td><td>最大载重量</td></tr>'
      }
      // 循环遍历，每行加入tr标签，每个单元格加td标签
      for (let i = 0; i < jsonData.length; i++) {
        str += '<tr>'
        for (let item in jsonData[i]) {
          // 增加\t为了不让表格显示科学计数法或者其他格式
          str += `<td>${jsonData[i][item] + '\t'}</td>`
        }
        str += '</tr>'
      }
      // Worksheet名
      let worksheet = 'Sheet1'
      let uri = 'data:application/vnd.ms-excel;base64,'
      // 下载的表格模板数据
      let template = `<html xmlns:o="urn:schemas-microsoft-com:office:office"
      xmlns:x="urn:schemas-microsoft-com:office:excel"
      xmlns="http://www.w3.org/TR/REC-html40">
      <head><!--[if gte mso 9]><xml><x:ExcelWorkbook><x:ExcelWorksheets><x:ExcelWorksheet>
        <x:Name>${worksheet}</x:Name>
        <x:WorksheetOptions><x:DisplayGridlines/></x:WorksheetOptions></x:ExcelWorksheet>
        </x:ExcelWorksheets></x:ExcelWorkbook></xml><![endif]-->
        </head><body><table>${str}</table></body></html>`
      // 下载模板
      window.location.href = uri + this.base64(template)
    }
  }
}
</script>

<style scoped>

</style>

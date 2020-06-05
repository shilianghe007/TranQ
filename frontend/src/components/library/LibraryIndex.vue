<template>
<div class="container-fluid">
<div class="row">
  <div class="col-md-12" style="margin-top: 35px">
    <h3>
      第一步：设置配送点
    </h3>
    <el-form :model="dynamicValidateFormLoc" ref="dynamicValidateFormLoc" label-width="120px" class="demo-dynamic">
      <el-row>
        <el-col :span="8"><div class="grid-content bg-purple">
          <el-form-item
        prop="centerx"
        label="配送中心x坐标"
        :rules="[
          { required: true, message: '请输入坐标', trigger: 'blur' },
          { type: 'string', message: '请输入正确的坐标', trigger: ['blur', 'change'] }
        ]"
      >
        <el-input v-model="dynamicValidateFormLoc.centerx"></el-input>
      </el-form-item>
        </div></el-col>
        <el-col :span="8"><div class="grid-content bg-purple-light">
          <el-form-item
        prop="centery"
        label="配送中心y坐标"
        :rules="[
          { required: true, message: '请输入坐标', trigger: 'blur' },
          { type: 'string', message: '请输入正确的坐标', trigger: ['blur', 'change'] }
        ]"
      >
        <el-input v-model="dynamicValidateFormLoc.centery"></el-input>
      </el-form-item>
        </div></el-col>
      </el-row>
      <el-row
        v-for="(location, index) in dynamicValidateFormLoc.locations"
      :key="location.key">
        <el-col :span="8"><div class="grid-content bg-purple">
          <el-form-item
        :label="'配送点' + index + 'x坐标'"
        :rules="{
          required: true, message: '配送点坐标不能为空', trigger: 'blur'
        }"
      >
        <el-input v-model="location.valuex"></el-input><el-button @click.prevent="removeitem(location, 0)">删除</el-button>
      </el-form-item>
        </div></el-col>
         <el-col :span="8"><div class="grid-content bg-purple">
          <el-form-item
        :label="'配送点' + index + 'y坐标'"
        :rules="{
          required: true, message: '配送点坐标不能为空', trigger: 'blur'
        }"
      >
        <el-input v-model="location.valuey"></el-input><el-button @click.prevent="removeitem(location, 0)">删除</el-button>
      </el-form-item>
        </div></el-col>
        <el-col :span="8"><div class="grid-content bg-purple">
          <el-form-item
        :label="'配送点' + index + '需求量'"
        :rules="{
          required: true, message: '配送点需求不能为空', trigger: 'blur'
        }"
      >
        <el-input v-model="location.need"></el-input><el-button @click.prevent="removeitem(location, 0)">删除</el-button>
      </el-form-item>
        </div></el-col>
      </el-row>
      <el-form-item>
        <el-button type="primary" @click="additem(0)">新增配送点</el-button>
        <!--<el-button @click="resetForm('dynamicValidateFormLoc')">批量导入</el-button>-->
        <el-button @click="resetForm('dynamicValidateFormLoc')">重置</el-button>
      </el-form-item>
    </el-form>
  </div>
</div>
<div class="row">
  <div class="col-md-12" style="margin-top: 15px">
    <uploader :options="options_loc" class="uploader-example">
      <uploader-unsupport></uploader-unsupport>
      <uploader-drop>
        <p>拖拽Excel表格文件至此以批量导入</p>
        <uploader-btn>选择文件</uploader-btn>
        <button class="getFileR" @click="getFileResult(0)">提取数据</button>
        <br/>
        <a @click="tableToExcel(0)" style="color: #3a8ee6;">点击此处下载样例模板</a>
        <!--<uploader-btn :attrs="attrs">select images</uploader-btn>-->
        <!--<uploader-btn :directory="true">select folder</uploader-btn>-->
      </uploader-drop>
      <uploader-list></uploader-list>
    </uploader>
  </div>
</div>
<div class="row">
  <div class="col-md-12" style="margin-top: 35px">
    <h3 class="text-left">
      第二步：设置配送车辆
    </h3>
    <el-form :model="dynamicValidateFormCar" ref="dynamicValidateFormCar" label-width="120px" class="demo-dynamic">
      <el-row
          v-for="(car, index) in dynamicValidateFormCar.cars"
        :key="car.key">
          <el-col :span="12"><div class="grid-content bg-purple">
            <el-form-item
          :label="'车型' + index + '数量'"
          :rules="{
            required: true, message: '数量不能为空', trigger: 'blur'
          }"
        >
          <el-input v-model="car.number"></el-input><el-button @click.prevent="removeitem(car, 1)">删除</el-button>
        </el-form-item>
          </div></el-col>
           <el-col :span="12"><div class="grid-content bg-purple">
            <el-form-item
          :label="'车型' + index + '限载量'"
          :rules="{
            required: true, message: '限载不能为空', trigger: 'blur'
          }"
        >
          <el-input v-model="car.weight"></el-input><el-button @click.prevent="removeitem(car, 1)">删除</el-button>
        </el-form-item>
          </div></el-col>
        </el-row>
      <el-form-item>
        <el-button type="primary" @click="additem(1)">新增车型</el-button>
        <!--<el-button @click="resetForm('dynamicValidateFormLoc')">批量导入</el-button>-->
        <el-button @click="resetForm('dynamicValidateFormCar')">重置</el-button>
      </el-form-item>
    </el-form>
  </div>
</div>
<div class="row">
  <div class="col-md-12">
    <uploader :options="options_car" class="uploader-example">
      <uploader-unsupport></uploader-unsupport>
      <uploader-drop>
        <p>拖拽Excel表格文件至此以批量导入</p>
        <uploader-btn>选择文件</uploader-btn>
        <button class="getFileR" @click="getFileResult(1)">提取数据</button>
        <br/>
        <a @click="tableToExcel(1)" style="color: #3a8ee6;">点击此处下载样例模板</a>
        <!--<uploader-btn :attrs="attrs">select images</uploader-btn>-->
        <!--<uploader-btn :directory="true">select folder</uploader-btn>-->
      </uploader-drop>
      <uploader-list></uploader-list>
    </uploader>
  </div>
</div>
<div class="row">
  <div class="col-md-12" style="margin-top: 35px">
    <h3 class="text-left">
      最后：设置算法参数
    </h3>
    <p style="margin-left: 10px;font-size: 15px;color: #1d1e1f">(可以直接跳过，接受默认参数)</p>
    <el-form :model="dynamicValidateFormParameter" ref="dynamicValidateFormParameter" label-width="120px" class="demo-dynamic">
      <el-row>
          <el-col :span="12"><div class="grid-content bg-purple">
            <el-form-item
          :label="'种群规模'"
          :rules="{
            required: true, message: '规模不能为空', trigger: 'blur'
          }"
        >
          <el-input v-model="dynamicValidateFormParameter.N"></el-input>
        </el-form-item>
          </div></el-col>
        <el-col :span="12"><div class="grid-content bg-purple">
            <el-form-item
          :label="'迭代次数'"
          :rules="{
            required: true, message: '此处不能为空', trigger: 'blur'
          }"
        >
          <el-input v-model="dynamicValidateFormParameter.iteration"></el-input>
        </el-form-item>
          </div></el-col>
        </el-row>
      <el-row>
          <el-col :span="12"><div class="grid-content bg-purple">
            <el-form-item
          :label="'变异概率'"
          :rules="{
            required: true, message: '此处不能为空', trigger: 'blur'
          }"
        >
          <el-input v-model="dynamicValidateFormParameter.muteProb"></el-input>
        </el-form-item>
          </div></el-col>
           <el-col :span="12"><div class="grid-content bg-purple">
            <el-form-item
          :label="'交叉概率'"
          :rules="{
            required: true, message: '此处不能为空', trigger: 'blur'
          }"
        >
          <el-input v-model="dynamicValidateFormParameter.crossProb"></el-input>
        </el-form-item>
          </div></el-col>
        </el-row>
      <el-form-item>
        <el-button type="primary" @click="submitForm('dynamicValidateFormCar')">提交</el-button>
        <el-button @click="resetForm('dynamicValidateFormParameter')">重置</el-button>
      </el-form-item>
    </el-form>
  </div>
</div>
</div>
</template>

<script>
/* eslint-disable camelcase,no-unused-expressions */

export default {
  name: 'AppLibrary',
  data () {
    return {
      options_loc: {
        target: 'http://182.92.236.19:8000/api/post_loc_file',
        testChunks: false
      },
      options_car: {
        target: 'http://182.92.236.19:8000/api/post_car_file',
        testChunks: false
      },
      attrs: {
        accept: 'image/*'
      },
      dynamicValidateFormLoc: {
        locations: [{
          valuex: '',
          valuey: '',
          need: ''
        }],
        centerx: '',
        centery: ''
      },
      dynamicValidateFormCar: {
        cars: [{
          number: '',
          weight: ''
        }]
      },
      dynamicValidateFormParameter: {
        N: 200,
        crossProb: 0.4,
        muteProb: 0.15,
        iteration: 150,
        punishment: 200
      }
    }
  },
  mounted: function () {
    if (this.$store.state.location !== '') {
      this.dynamicValidateFormLoc = this.$store.state.location
    }
    if (this.$store.state.car !== '') {
      this.dynamicValidateFormCar = this.$store.state.car
    }
  },
  methods: {
    getFileResult (type) {
      var result = ''
      var _this = this
      this.$axios
        .get('/get_file_result', {
          params: {
            type: type
          }
        })
        .then(function (response) {
          console.log(1)
          if (response.data.error_num === 0) {
            result = response.data.msg
            console.log(result)
            _this.test()
            var result_array = []
            var temp_result = []
            if (type === 0) {
              _this.dynamicValidateFormLoc.locations = []
              let index = 0
              let num = 0
              let temp_single = ''
              while (index < result.length) {
                if (result.charAt(index) !== '#') {
                  temp_single += result.charAt(index)
                  index++
                } else {
                  temp_result = temp_result.concat([parseFloat(temp_single)])
                  temp_single = ''
                  num++
                  if (num === 3) {
                    console.log(temp_result)
                    result_array = result_array.concat([temp_result])
                    temp_result = []
                    num = 0
                  }
                  index++
                }
              }
              _this.dynamicValidateFormLoc.centerx = result_array[0][0] + ''
              _this.dynamicValidateFormLoc.centery = result_array[0][1] + ''
              for (let i = 1; i < result_array.length; i++) {
                _this.dynamicValidateFormLoc.locations.push({
                  valuex: result_array[i][0],
                  valuey: result_array[i][1],
                  need: result_array[i][2]
                })
              }
            } else {
              _this.dynamicValidateFormCar.cars = []
              let index = 0
              let num = 0
              let temp_single = ''
              while (index < result.length) {
                if (result.charAt(index) !== '#') {
                  temp_single += result.charAt(index)
                  index++
                } else {
                  temp_result = temp_result.concat([parseFloat(temp_single)])
                  temp_single = ''
                  num++
                  if (num === 2) {
                    result_array = result_array.concat([temp_result])
                    temp_result = []
                    num = 0
                  }
                  index++
                }
              }
              for (let i = 0; i < result_array.length; i++) {
                _this.dynamicValidateFormCar.cars.push({
                  number: result_array[i][0],
                  weight: result_array[i][1]
                })
              }
            }
          }
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    test () {
      console.log('test')
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
    },
    // 输出base64编码
    base64 (s) { return window.btoa(unescape(encodeURIComponent(s))) },
    submitForm (formName) {
      this.$store.commit('setLength', '') // 初始化
      this.$store.commit('setIterNum', this.dynamicValidateFormParameter.iteration) // 初始化
      this.$refs[formName].validate((valid) => {
        if (valid) {
          alert('submit!')
          var _this = this
          _this.$store.commit('setLocs', _this.dynamicValidateFormLoc)
          _this.$store.commit('setCars', _this.dynamicValidateFormCar)
          // 对输入数据进行预处理，以符合接口的数据格式
          var car_number = 0
          for (var i = 0; i < this.dynamicValidateFormCar.cars.length; i++) {
            car_number = parseInt(car_number) + parseInt(this.dynamicValidateFormCar.cars[i].number)
          }
          var m_max = ''
          for (var j = 0; j < this.dynamicValidateFormCar.cars.length; j++) {
            m_max += '%#'
            m_max += this.dynamicValidateFormCar.cars[j].weight
            m_max += '#'
            m_max += this.dynamicValidateFormCar.cars[j].number
          }
          var city_number = this.dynamicValidateFormLoc.locations.length
          _this.$store.commit('setCityNum', city_number)
          var N = this.dynamicValidateFormParameter.N
          var crossProb = this.dynamicValidateFormParameter.crossProb
          var muteProb = this.dynamicValidateFormParameter.muteProb
          var iteration = this.dynamicValidateFormParameter.iteration
          var punishment = 200
          var location = ''
          for (var k = 0; k < this.dynamicValidateFormLoc.locations.length; k++) {
            location += '%#'
            location += this.dynamicValidateFormLoc.locations[k].valuex
            location += '#'
            location += this.dynamicValidateFormLoc.locations[k].valuey
            location += '#'
            location += this.dynamicValidateFormLoc.locations[k].need
          }
          var center = this.dynamicValidateFormLoc.centerx + '#' + this.dynamicValidateFormLoc.centery
          this.$axios
            .get('/add_instance', {
              params: {
                Car_Number: car_number,
                Dis_max: 50,
                M_max: m_max,
                City_Number: city_number,
                N: N,
                crossProb: crossProb,
                muteProb: muteProb,
                iteration: iteration,
                punishment: punishment,
                Location: location,
                center: center
                // Car_Number = 10  # 汽车数量
                // Dis_max = 25  # 车辆最大行驶距离
                // M_max = np.mat([[5, 5], [8, 5]])  # 最大载重量
                // City_Number = 20  # 需求点数量
                // N = 150  # 群体规模
                // crossProb = 0.4  # 交叉概率
                // muteProb = 0.1  # 变异概率
                // iteration = 200  # 迭代次数
                // punishment = 200  # 惩罚权重
                // width = 10  # 范围
                // Location = np.random.random((City_Number, 2)) * width  # 随机生成坐标点
                // center = np.mat([width / 2, width / 2])  # 配送中心坐标
                // M = np.random.random((1, City_Number)) * 3  # 随机生成各点需求量
              }
            })
            .then(function (response) {
              console.log(response)
              if (response.data.error_num === 0) {
                _this.$store.commit('setToken', response.data.token)
              }
            })
            .catch(function (error) {
              console.log(error)
            })
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    resetForm (formName) {
      if (formName === 'dynamicValidateFormLoc') {
        this.dynamicValidateFormLoc.locations = []
        this.dynamicValidateFormLoc.centerx = ''
        this.dynamicValidateFormLoc.centery = ''
      } else if (formName === 'dynamicValidateFormCar') {
        this.dynamicValidateFormCar.cars = []
      }
    },
    removeitem (item, a) {
      if (a === 0) {
        var index = this.dynamicValidateFormLoc.locations.indexOf(item)
        if (index !== -1) {
          this.dynamicValidateFormLoc.locations.splice(index, 1)
        }
      } else {
        index = this.dynamicValidateFormCar.cars.indexOf(item)
        if (index !== -1) {
          this.dynamicValidateFormCar.cars.splice(index, 1)
        }
      }
    },
    additem (a) {
      if (a === 0) {
        this.dynamicValidateFormLoc.locations.push({
          valuex: '',
          valuey: '',
          need: '',
          key: Date.now()
        })
      } else {
        this.dynamicValidateFormCar.cars.push({
          number: '',
          weight: '',
          key: Date.now()
        })
      }
    }
  }
}
</script>

<style scoped>
  .uploader-example {
      width: 1280px;
      padding: 15px;
      margin: 10px auto 0;
      font-size: 14px;
      box-shadow: 0 0 10px rgba(0, 0, 0, .4);
      text-align: center;
  }
  .uploader-example .uploader-btn {
    margin-right: 4px;
  }
  .uploader-example .uploader-list {
    max-height: 440px;
    overflow: auto;
    overflow-x: hidden;
    overflow-y: auto;
  }
  .getFileR {
    display: inline-block;
    position: relative;
    padding: 4px 8px;
    font-size: 100%;
    line-height: 1.4;
    color: #666;
    border: 1px solid #666;
    cursor: pointer;
    border-radius: 2px;
    background: none;
    outline: none;
  }
</style>

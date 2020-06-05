<template>
<div class="container-fluid">
<div class="row">
  <div class="col-md-12">
    <div class="carousel slide" id="carousel-12641">
      <ol class="carousel-indicators">
        <li data-slide-to="0" data-target="#carousel-12641" class="active">
        </li>
        <li data-slide-to="1" data-target="#carousel-12641">
        </li>
        <li data-slide-to="2" data-target="#carousel-12641">
        </li>
      </ol>
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img class="d-block w-100" alt="Carousel Bootstrap First" src="https://www.layoutit.com/img/sports-q-c-1600-500-1.jpg" />
          <div class="carousel-caption">
            <h3>
              配送规划工具
            </h3>
            <p>
              帮助企业极大地优化配送路线，降低配送成本，绝对的配送规划利器
            </p>
          </div>
        </div>
        <div class="carousel-item">
          <img class="d-block w-100" alt="Carousel Bootstrap Second" src="https://www.layoutit.com/img/sports-q-c-1600-500-2.jpg" />
          <div class="carousel-caption">
            <h4>
              Second Thumbnail label
            </h4>
            <p>
              Cras justo odio, dapibus ac facilisis in, egestas eget quam. Donec id elit non mi porta gravida at eget metus. Nullam id dolor id nibh ultricies vehicula ut id elit.
            </p>
          </div>
        </div>
        <div class="carousel-item">
          <img class="d-block w-100" alt="Carousel Bootstrap Third" src="https://www.layoutit.com/img/sports-q-c-1600-500-3.jpg" />
          <div class="carousel-caption">
            <h4>
              Third Thumbnail label
            </h4>
            <p>
              Cras justo odio, dapibus ac facilisis in, egestas eget quam. Donec id elit non mi porta gravida at eget metus. Nullam id dolor id nibh ultricies vehicula ut id elit.
            </p>
          </div>
        </div>
      </div> <a class="carousel-control-prev" href="#carousel-12641" data-slide="prev"><span class="carousel-control-prev-icon"></span> <span class="sr-only">Previous</span></a> <a class="carousel-control-next" href="#carousel-12641" data-slide="next"><span class="carousel-control-next-icon"></span> <span class="sr-only">Next</span></a>
    </div>
  </div>
</div>
<div class="row" style="margin-top: 10px">
  <div class="col-md-12">
    <div class="jumbotron" style="line-height: 35px;text-align: center">
      <h2>
        TranQ
      </h2>
      <p>
        运用遗传算法等智能算法对配送问题进行精确的数学建模，迅速得到优质的路径规划方案。<br/>在这里，只需输入配送点和运输车辆等配置信息，系统将为您一键搞定路径规划，并动态地将迭代信息和最终方案可视化呈现！
      </p>
      <p>
        <a class="btn btn-primary btn-large" @click="Go()" style="color: white">开始规划</a>
      </p>
    </div>
  </div>
</div>
<div class="row">
  <div class="col-md-4">
    <div class="card">
      <img class="card-img-top" alt="Bootstrap Thumbnail First" src="https://www.layoutit.com/img/people-q-c-600-200-1.jpg">
      <div class="card-block">
        <h5 class="card-title">
          输入（输出）批量导入（导出）
        </h5>
        <p class="card-text">
          配送点和配送车辆设置信息太多？没关系，直接一键批量导入！点击下方查看具体步骤。
        </p>
        <p>
          <a class="btn btn-primary" @click="openUpload()" style="color: white">批量导入</a>
        </p>
      </div>
    </div>
  </div>
  <div class="col-md-4">
    <div class="card">
      <img class="card-img-top" alt="Bootstrap Thumbnail Second" src="https://www.layoutit.com/img/city-q-c-600-200-1.jpg">
      <div class="card-block">
        <h5 class="card-title">
          智能算法助阵
        </h5>
        <p class="card-text">
          核心以遗传算法为基础，蚁群算法进行辅助微调，并使用DP算法进行算力优化，快准稳！
        </p>
        <p>
          <a class="btn btn-primary" @click="openSuanfa()" style="color: white">智能算法</a>
        </p>
      </div>
    </div>
  </div>
  <div class="col-md-4">
    <div class="card">
      <img class="card-img-top" alt="Bootstrap Thumbnail Third" src="https://www.layoutit.com/img/sports-q-c-600-200-1.jpg">
      <div class="card-block">
        <h5 class="card-title">
          动态呈现与可视化表达
        </h5>
        <p class="card-text">
          动态跟踪遗传算法的每一次迭代结果，通过将数据可视化呈现带来准确的结果展现！
        </p>
        <p>
          <a class="btn btn-primary"  @click="openDynamic()" style="color: white">动态呈现</a>
        </p>
      </div>
    </div>
  </div>
</div>
<div class="row" style="margin-top: 15px">
  <div class="col-md-4">
    <h2 style="margin-left: 10px">
      GitHub
    </h2>
    <p style="margin-left: 10px">
      本项目的主要技术栈包括python、Django、Vue、Mysql、celery，代码等工程文件已上传至Github库中，欢迎为我们的网站提出您的宝贵意见！
    </p>
    <p>
      <a class="btn" href="https://github.com/whustone007/TranQ">查看代码 »</a>
    </p>
  </div>
  <div class="col-md-4">
    <h2 style="margin-left: 10px">
      关于我们
    </h2>
    <p style="margin-left: 10px">
      一群爱捣鼓技术的年轻人，同时渴望用自己的力量为世界带来些许不同。代码就是我们改变世界的有力武器。我们使用程序优化配送路径，希望能够为配送行业做出我们的努力！
    </p>
    <p>
      <a class="btn" @click="openUs()" style="color: blue">我们是谁 »</a>
    </p>
  </div>
  <div class="col-md-4">
    <h2 style="margin-left: 10px">
      加入我们
    </h2>
    <p style="margin-left: 10px">
      欢迎加入我们，成为TranQ团队的建设者，为网站的进一步开发添砖加瓦。在这里，我们能为您提供智能算法、数学建模、机器学习、网站开发等多方面大展身手的舞台！
    </p>
    <p>
      <a class="btn" @click="openConnect()" style="color: blue">联系我们 »</a>
    </p>
  </div>
</div>
</div>
</template>

<script>
export default {
  name: 'Cover',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      carouselNum: 0
    }
  },
  methods: {
    Go () {
      this.$router.push('/parameter')
    },
    openUpload () {
      this.$alert('在配置配送车辆、需求点等参数时，可以支持配置文件批量导入数据的形式完成。首先点击“选择文件”上传配置文件，然后点击提取数据即可。如果不知道配置文件的格式，可以下载模板文件哦~', '批量导入', {
        confirmButtonText: '确定',
        callback: action => {}
      })
    },
    openSuanfa () {
      this.$alert('遗传算法是计算数学中用于解决最优化的搜索算法，是进化算法的一种。进化算法最初是借鉴了进化生物学中的一些现象而发展起来的，这些现象包括遗传、突变、自然选择以及杂交等。遗传算法通常实现方式为一种计算机模拟。对于一个最优化问题，一定数量的候选解（称为个体）的抽象表示（称为染色体）的种群向更好的解进化。传统上，解的编码用二进制表示（即0和1的串），但也可以用其他表示方法（我们的算法就是非二进制表示）。进化从完全随机个体的种群开始，之后一代一代发生。在每一代中，整个种群的适应度被评价，从当前种群中基于它们的适应度随机地选择多个个体，通过自然选择和突变产生新的生命种群，该种群在算法的下一次迭代中成为当前种群。\n' +
        '在我们的项目实现里，遗传算法中的一个个体就代表了一种可能的路径规划，一个个体的编码包含了所有车辆的路线信息。通过多次的迭代，最终得到优质的个体，即优质的路线规划。', '智能算法', {
        confirmButtonText: '确定',
        callback: action => {}
      })
    },
    openDynamic () {
      this.$alert('用户可以动态地查看每一次迭代情况，后台数据库存储每一次记录，做到记录可查。', '动态展示', {
        confirmButtonText: '确定',
        callback: action => {}
      })
    },
    openUs () {
      this.$alert('一群想要成为技术大牛和亿万富翁的coder', '关于我们', {
        confirmButtonText: '确定',
        callback: action => {}
      })
    },
    openConnect () {
      this.$alert('将您的简历投递至邮箱（2020520@qq.com），我们会及时回复！', '批量导入', {
        confirmButtonText: '确定',
        callback: action => {}
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>

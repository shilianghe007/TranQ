<template>
    <el-menu
      :default-active="'/index'"
      router
      mode="horizontal"
      background-color="white"
      text-color="#222"
      active-text-color="red"
      style="min-width: 1300px">
      <el-menu-item v-for="(item,i) in navList" :key="i" :index="item.name" style="font-size:15px">
        {{ item.navItem }}
      </el-menu-item>
      <!--<a href="#nowhere" style="color: #222;float: right;padding: 20px;">更多功能</a>-->
      <img style="float:right;padding-top: 8px;width: 50px;height: 55px;margin-right: 20px"
        src="../../assets/logo.png"
        alt="Grapefruit slice atop a pile of other slices">
      <span style="position: absolute;padding-top: 20px;right: 40%;font-size: 20px;font-weight: bold">TranQ - 配送路径规划助手</span>
    </el-menu>
</template>

<script>
export default {
  name: 'NavMenu',
  data () {
    return {
      navList: [
        {name: '/index', navItem: '首页'},
        {name: '/parameter', navItem: '设置'},
        {name: '/presentation', navItem: '迭代展示'},
        {name: '/admin', navItem: '个人中心'}
      ]
    }
  }
}
</script>

<style scoped>
  a{
    text-decoration: none;
  }

  span {
    pointer-events: none;
  }
</style>

<template>
  <div>
    <h4 style="margin-top: 15px;text-align: center">用户信息</h4>
    <hr style="height:1px;border:none;border-top:1px solid #2b82ff;" />
    <div style="text-align: center;">
      <div style="margin-bottom: 10px">
        <font face="宋体" color="black" size="4">昵称：张小帅</font>
        <button class="change" style="margin-left: 340px">修改</button>
      </div>
      <div style="margin-bottom: 10px">
        <font face="宋体" color="black" size="4">账号：1421553</font>
        <button class="change" style="margin-left: 330px">修改</button>
      </div>
      <div style="margin-bottom: 10px">
        <font face="宋体" color="black" size="4">密码：********</font>
        <button class="change" style="margin-left: 320px">修改</button>
      </div>
      <div style="margin-bottom: 10px">
        <font face="宋体" color="black" size="4">企业（团体名称）：东风速运公司</font>
        <button class="change" style="margin-left: 175px">修改</button>
      </div>
      <div style="margin-bottom: 10px">
        <font face="宋体" color="black" size="4">邮箱：{{email}}</font>
        <button class="change" style="margin-left: 240px" @click="open()">修改</button>
      </div>
      <div style="margin-bottom: 10px">
        <font face="宋体" color="black" size="4">道路运输经营许可证号：115312564264</font>
        <button class="change" style="margin-left: 140px">修改</button>
      </div>
      <button class="change" @click="logout()">退出登录</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UserIndex',
  data () {
    return {
      options: {
        target: 'http://182.92.236.19:8000/api/get_file',
        testChunks: false
      },
      email: '1213816796@qq.com',
      attrs: {
        accept: '*.txt'
      }
    }
  },
  methods: {
    open () {
      this.$prompt('请输入邮箱', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        inputPattern: /[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?/,
        inputErrorMessage: '邮箱格式不正确'
      }).then(({ value }) => {
        this.email = value
        this.$message({
          type: 'success',
          message: '你的新邮箱是: ' + value
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '取消输入'
        })
      })
    },
    logout () {
      this.$alert('您确定要登出吗？', '确认', {
        confirmButtonText: '确定',
        callback: action => {
          this.$message({
            type: 'info',
            message: `action:${action}`
          })
          if (action === 'confirm') {
            window.localStorage.removeItem('user')
            this.$message({
              type: 'info',
              message: '已退出登录'
            })
          }
        }
      })
    }
  }
}
</script>

<style scoped>
  .uploader-example {
    width: 880px;
    padding: 15px;
    margin: 40px auto 0;
    font-size: 12px;
    box-shadow: 0 0 10px rgba(0, 0, 0, .4);
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
  .change {
    display: inline-block;
    position: relative;
    padding: 4px 8px;
    font-size: 90%;
    line-height: 1.4;
    color: #666;
    border: 1px solid #666;
    cursor: pointer;
    border-radius: 2px;
    background: none;
    outline: none;
  }
</style>

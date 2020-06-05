<template>
  <body id="poster">
    <el-form class="login-container" label-position="left"
             label-width="0px">
      <h3 class="login_title">系统登录</h3>
      <el-form-item>
        <el-input type="text" v-model="loginForm.username"
                  auto-complete="off" placeholder="账号"></el-input>
      </el-form-item>
      <el-form-item>
        <el-input type="password" v-model="loginForm.password"
                  auto-complete="off" placeholder="密码"></el-input>
      </el-form-item>
      <el-form-item style="width: 100%">
        <el-button type="primary" style="width: 100%;background: #505458;border: none" v-on:click="login">登录</el-button>
      </el-form-item>
    </el-form>
  </body>
</template>

<script>

export default {
  name: 'Login',
  data () {
    return {
      loginForm: {
        username: '22',
        password: '33'
      },
      responseResult: []
    }
  },
  methods: {
    // login () {
    //   var _this = this
    //   console.log(this.$store.state)
    //   this.$axios
    //     .get('/login_user', {
    //       params: {
    //         user_name: this.loginForm.username,
    //         user_ps: this.loginForm.password
    //       }
    //     })
    //     .then(successResponse => {
    //       console.log(successResponse)
    //       if (successResponse.data.error_num === 0) {
    //         // var data = this.loginForm
    //         _this.$store.commit('login', _this.loginForm)
    //         var path = this.$route.query.redirect
    //         this.$router.replace({path: path === '/' || path === undefined ? '/index' : path})
    //       }
    //     })
    //     .catch(failResponse => {
    //     })
    // }
    login () {
      var _this = this
      console.log(this.$store.state)
      this.$axios
        .post('/login', {
          username: 'Cliff',
          password: 123456
        })
        .then(successResponse => {
          console.log(successResponse)
          if (successResponse.data.code === 200) {
            // var data = this.loginForm
            _this.$store.commit('login', _this.loginForm)
            var path = this.$route.query.redirect
            this.$router.replace({path: path === '/' || path === undefined ? '/index' : path})
          }
        })
        .catch(failResponse => {
        })
    }
  }
}
</script>

<style>
    #poster {
    background:url("../assets/eva.jpg") no-repeat;
    background-position: center;
    height: 100%;
    width: 100%;
    background-size: cover;
    position: fixed;
  }
  body{
    margin: 0px;
  }
  .login-container {
    border-radius: 15px;
    background-clip: padding-box;
    margin: 90px auto;
    width: 350px;
    padding: 35px 35px 15px 35px;
    background: #fff;
    border: 1px solid #eaeaea;
    box-shadow: 0 0 25px #cac6c6;
  }
  .login_title {
    margin: 0px auto 40px auto;
    text-align: center;
    color: #505458;
  }
</style>

<template>
  <div id="bigBox">
    <h1>智慧养老</h1>
    <div class="inputBox">
      <div class="inputText">
        <span class="iconfont icon-nickname"></span>
        <input type="text" placeholder="用  户  名" v-model="exam.id"/>
      </div>
      <div class="inputText">
        <span class="iconfont icon-visible"></span>
        <input type="password" placeholder="密  码" v-model="exam.password" />
      </div>
    </div>
    <input class="loginButton" type="button" value="登  录" @click="loginning()"/>
  </div>
</template>

<script>
import "../css/style.css"
export default {
  data() {
    return {
      exam: {
        id: '',
        password: ''
      }
    }
  },
  methods: {
    async loginning() {
      this.$axios.post(`http://127.0.0.1:5000/login`, this.exam).then((res)=>{
        console.log(res);
        if (res.data == 0) {
          this.$message({
            showClose: true,
            message: '用户名或密码错误，请核对后重新输入！',
            type: 'error'
          });
        }
        else {
          this.$router.push('home');
        }
      });
    }
  }
}
</script>


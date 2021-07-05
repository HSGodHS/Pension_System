<template>
  <el-container direction="vertical">

    <navMenu width="100%"></navMenu>

    <el-container direction="horizontal">
      <el-aside width="280px">
        <sideBar class="menu"></sideBar>
      </el-aside>
      <el-main>
        <el-form label-position="left" label-width="0px" class="login-form">
          <el-form-item prop="old_pass">
            <el-input v-model="exam.old_pass" type="text" auto-complete="off" placeholder="原密码" show-password>
              <svg-icon slot="prefix" icon-class="user" class="el-input__icon input-icon" />
            </el-input>
          </el-form-item>
          <el-form-item prop="new_pass">
            <el-input v-model="exam.new_pass" type="text" auto-complete="off" placeholder="新密码" show-password>
              <svg-icon slot="prefix" icon-class="password" class="el-input__icon input-icon" />
            </el-input>
          </el-form-item>
          <el-form-item prop="conf_pass">
            <el-input v-model="exam.conf_pass" type="text" auto-complete="off" placeholder="确认密码" show-password>
              <svg-icon slot="prefix" icon-class="password" class="el-input__icon input-icon" />
            </el-input>
          </el-form-item>
          <el-form-item style="width:100%;">
            <el-button :loading="loading" size="medium" type="primary" style="width:100%;" @click="updatePass()" >
              <span>确  认</span>
            </el-button>
          </el-form-item>
        </el-form>
      </el-main>
    </el-container>
  </el-container>

</template>

<script>
export default {
  data() {
    return {
      exam: {
        old_pass: '',
        new_pass: '',
        conf_pass: ''
      }
    }
  },
  methods:{
    async updatePass() {
      this.$axios.post(`http://127.0.0.1:5000/updatepass`, this.exam).then((res)=>{
          console.log(res);
          if (res.data == 0) {
            alert("修改成功,点击确定返回登陆界面。")
            this.$router.push({path:'/login'});
          }
          else if(res.data == 1){
            alert("修改失败，原密码不正确!")
          }
          else if(res.data == 2){
            alert("两次密码输入不一致，请检查后重新输入!")
          }


      });
    }
  }
}
</script>

<template>
  <div class="headerBody">
    <div class="title">
      <el-row :gutter="20">
        <el-col :span="4">
<!--          <img src="../assets/img/img.jpg" />-->
          <img style="width: 200px;margin: 10px auto auto 20px" src="../static/logo.png" />
        </el-col>
      </el-row>
    </div>

    <div class="header-right">
      <div class="header-user-con">
        <!-- 用户头像 -->
        <div class="user-avator">
          <img src="../assets/img/img.jpg" />
        </div>
        <!-- 用户名下拉菜单 -->
        <el-dropdown class="user-name" trigger="click" @command="handleCommand">
                    <span class="el-dropdown-link">
                        <i class="el-icon-caret-bottom"></i>
                    </span>
          <template #dropdown>
            <el-dropdown-menu>
              <a target="_blank">
                <el-dropdown-item divided command="update">修改密码</el-dropdown-item>
              </a>
              <el-dropdown-item divided command="loginout">退出登录</el-dropdown-item>
            </el-dropdown-menu>
          </template>
        </el-dropdown>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "navMenu",
  methods: {
    // 用户名下拉菜单选择事件
    handleCommand(command) {
      if (command == "loginout") {
        localStorage.removeItem("ms_username");
        this.$router.push("/login");
      }
      if (command == "update") {
        localStorage.removeItem("ms_username");
        this.$router.push("/user/updatepass");
      }
    }
  }
}
</script>

<style scoped>

.headerBody{
  height: 80px;
  display: flex;
  background-color: #018675;
  margin-left: 0px;
}
.title{
  font-size: 18px;
  width: 85%;
  min-width: 400px;
  color: #E6E6E6;
}
.blank{
  margin: 20px;
}
.user-avator {
  margin-left: 20px;
}
.user-name {
  margin-left: 10px;
}
.user-avator img {
  display: block;
  width: 40px;
  height: 40px;
  border-radius: 50%;
}
.el-dropdown-link {
  color: #fff;
  cursor: pointer;
}
.header-right {
  float: right;
  padding-right: 50px;
}
.header {
  position: relative;
  box-sizing: border-box;
  width: 100%;
  height: 70px;
  font-size: 22px;
  color: #fff;
}
.collapse-btn {
  float: left;
  padding: 0 21px;
  cursor: pointer;
  line-height: 70px;
}
.header .logo {
  float: left;
  width: 250px;
  line-height: 70px;
}
.header-right {
  float: right;
  padding-right: 50px;
}
.header-user-con {
  display: flex;
  height: 70px;
  align-items: center;
}
.btn-fullscreen {
  transform: rotate(45deg);
  margin-right: 5px;
  font-size: 24px;
}
.btn-bell,
.btn-fullscreen {
  position: relative;
  width: 30px;
  height: 30px;
  text-align: center;
  border-radius: 15px;
  cursor: pointer;
}
.btn-bell-badge {
  position: absolute;
  right: 0;
  top: -2px;
  width: 8px;
  height: 8px;
  border-radius: 4px;
  background: #f56c6c;
  color: #fff;
}
.btn-bell .el-icon-bell {
  color: #fff;
}
</style>

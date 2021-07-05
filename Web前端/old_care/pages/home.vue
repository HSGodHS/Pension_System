<template>
  <el-container direction="vertical">

    <navMenu width="100%"></navMenu>

    <el-container direction="horizontal" style="height: 673px; background-image: url(static/background.png);background-size: cover" >
      <el-aside width="280px" height="100%">
        <sideBar class="menu" page-index="7" open-index="0" style="height: 100%"></sideBar>

      </el-aside>

      <el-main >
        <el-row :gutter="20">

          <el-col :span="14">

            <el-card shadow="hover" style="height:630px;">
              <template #header>
                <div class="clearfix">
                  <span style="font-size: 18px">系统简介</span>
                </div>
              </template>
              <p style="font-size: 18px; line-height: 45px">
                智慧养老是面向居家老人、社区及养老机构的传感网系统与信息平台，并在此基础上提供实时、快捷、高效、低成本的，物联化、互联化、智能化的养老服务。
                随着科技进步，新型养老方式日趋流行,社会上也涌现出一系列如只为父母设计的电视盒子等高科技产品，提升老人的晚年生活质量，最大程度的解决空巢老人寂寞的问题，是智慧养老，候鸟式养老，信息化养老，中国式养老的新形式。智慧养老经过一年多的良好运营与快速成长，获得了政府、行业、公众及媒体的广泛关注与认可。让老人充分享受物联网带来的便捷和舒适。
              </p>

            </el-card>
          </el-col>

          <el-col :span="10">
            <el-card shadow="hover" class="mgb20" style="height:252px;">
              <div class="user-info">
                <img src="../assets/img/img.jpg" class="user-avator" alt />
                <div class="user-info-cont">
                  <div style="font-size: 20px">工号：{{info.userName}}</div>
                  <div style="font-size: 20px">姓名：{{info.staffName}}</div>
                </div>
              </div>
            </el-card>
            <el-card shadow="hover" style="height:360px;">
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
              <el-image
                style="width: 330px; height: 350px"
                :src="require('../assets/img/cal.png')"
                :fit="fit"></el-image>
            </el-card>
          </el-col>

        </el-row>
      </el-main>
    </el-container>

  </el-container>

</template>

<script>
export default {
  name: "center",
  data() {
    return {
      info : []
    }
  },
  mounted() {
    var url=document.location.href;
    if (url.indexOf("yes=")==-1){
      var t= new Date();
      window.location.href = url + "?yes=" + t.getTime();
    }
    this.$axios.get(`http://127.0.0.1:5000/userName`).then((res) => {
      console.log(res.data);
      this.info=res.data[0];
      console.log(this.info);
    });
  }
}
</script>

<style scoped>
.el-row {
  margin-bottom: 20px;
}

.grid-content {
  display: flex;
  align-items: center;
  height: 100px;
}

.grid-cont-right {
  flex: 1;
  text-align: center;
  font-size: 14px;
  color: #999;
}

.grid-num {
  font-size: 30px;
  font-weight: bold;
}

.grid-con-icon {
  font-size: 50px;
  width: 100px;
  height: 100px;
  text-align: center;
  line-height: 100px;
  color: #fff;
}

.grid-con-1 .grid-con-icon {
  background: rgb(45, 140, 240);
}

.grid-con-1 .grid-num {
  color: rgb(45, 140, 240);
}

.grid-con-2 .grid-con-icon {
  background: rgb(100, 213, 114);
}

.grid-con-2 .grid-num {
  color: rgb(45, 140, 240);
}

.grid-con-3 .grid-con-icon {
  background: rgb(242, 94, 67);
}

.grid-con-3 .grid-num {
  color: rgb(242, 94, 67);
}

.user-info {
  display: flex;
  align-items: center;
  padding-bottom: 20px;
  border-bottom: 2px solid #ccc;
  margin-bottom: 20px;
}

.user-avator {
  width: 220px;
  height: 220px;
  border-radius: 50%;
}

.user-info-cont {
  padding-left: 50px;
  flex: 1;
  font-size: 14px;
  color: #999;
}

.user-info-cont div:first-child {
  font-size: 30px;
  color: #222;
}

.user-info-list {
  font-size: 14px;
  color: #999;
  line-height: 25px;
}

.user-info-list span {
  margin-left: 70px;
}

.mgb20 {
  margin-bottom: 20px;
}

.todo-item {
  font-size: 14px;
}

.todo-item-del {
  text-decoration: line-through;
  color: #999;
}

</style>

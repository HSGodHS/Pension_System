<template>
  <el-menu
    :default-active="activeIndex"
    :default-openeds="activeOpendsIndex"
    @open="handleOpen"
    @close="handleClose"
    background-color="#037163"
    text-color="#fff"
    active-text-color="#ffd04b"
    :unique-opened=true>


    <el-menu-item index="0" @click="$router.push({name:'home'})" >
      <i class="el-icon-s-home"></i>
      <span slot="title">首页</span>
    </el-menu-item>

    <el-menu-item index="1" @click="$router.push({name:'cameras'})">
      <i class="el-icon-camera-solid" ></i>
      <span slot="title">实时监测</span>
    </el-menu-item>

    <el-menu-item index="2" @click="$router.push({name:'old_people-old_people'})">
      <i class="el-icon-s-custom" ></i>
      <span slot="title">老人管理</span>
    </el-menu-item>

    <el-menu-item index="3" @click="$router.push({name:'staff'})">
      <i class="el-icon-s-platform" ></i>
      <span slot="title">员工管理</span>
    </el-menu-item>

    <el-menu-item index="4" @click="$router.push({name:'volunteers'})">
      <i class="el-icon-s-order" ></i>
      <span slot="title">义工管理</span>
    </el-menu-item>

    <el-menu-item index="5" @click="$router.push({name:'user-center'})">
      <i class="el-icon-s-tools" ></i>
      <span slot="title">用户管理</span>
    </el-menu-item>

  </el-menu>
</template>

<script>
export default {
  name: "sideBar",
  props:{
    /*
    * 外部输入目前显示的页面内容
    * */
    pageIndex: {
      type: String
    },
    openIndex: {
      type: String
    }
  },
  data() {
    return{
      activeIndex: '1',
      activeOpendsIndex: ['0'],
      authorization:{
        occupa_id: ''
      }
    }
  },
  methods: {
    handleOpen(key, keyPath) {
    },
    handleClose(key, keyPath) {
    }
  },
  created() {
    this.activeIndex = this.pageIndex;
    if (this.openIndex != '0') {
      this.activeOpendsIndex.pop();
      this.activeOpendsIndex.push(this.openIndex);
    }
    this.$axios.get(`http://127.0.0.1:5000/getAuthorization`).then((res) => {
      console.log(res);
      this.authorization = res.data[0]
    });
   }

}
</script>
<style>
span{
  font-size: 16px;
}
</style>

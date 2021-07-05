<template>
  <el-container direction="vertical">

    <navMenu width="100%"></navMenu>

    <el-container direction="horizontal">
      <el-aside width="230px" height="100%">
        <sideBar class="menu" page-index="6" open-index="0" ></sideBar>
      </el-aside>
      <el-main>

        <el-container direction="horizontal">
          <el-input v-model="words.word" placeholder="请输入检索工号（支持模糊查询）"></el-input>
          <el-button style="margin-left: 20px" @click="vague()">搜索</el-button>
        </el-container>

        <el-table
          :data="tableData.slice((currentPage-1)*pagesize,currentPage*pagesize)"
          height="502"
          style="width: 100%; margin-top: 20px">

          <el-table-column
            prop="staff_id"
            label="用户编号">
          </el-table-column>
          <el-table-column
            prop="user_id"
            label="用户名">
          </el-table-column>
          <el-table-column
            prop="password"
            label="登陆密码">
          </el-table-column>

          <el-table-column label="密码重置">
            <template slot-scope="scope">
              <el-button icon="el-icon-edit" circle size="small"
                         @click="handleEdit(scope.row)"></el-button>
            </template>
          </el-table-column>

        </el-table>

        <div style="text-align: center;margin-top: 20px;">
          <el-pagination
            background
            layout="prev, pager, next"
            :total="total"
            @current-change="current_change">
          </el-pagination>
        </div>


      </el-main>
    </el-container>
  </el-container>

</template>

<script>
import sideBar from "@/components/sideBar";
import navMenu from "@/components/navMenu";
export default {
  name: "risk",
  components: {sideBar, navMenu},
  data() {
    return {
      tableData: [],
      total: 0,
      pagesize: 8,
      currentPage: 1,
      words: {
        word: ''
      },
      drawer: false,
      direction: 'rtl',
      newData: {
        name: '',
        cpnt_name: '',
      },
      options: [{
        component_names: ''
      }],
      cpntData: {
        train: '',
        station: '',
        mileMark: ''
      }
    }
  },
  mounted() {
    this.$axios.get(`http://127.0.0.1:5000/identify`).then((res)=>{
      console.log(res);
      if (res.data == 0) {

        this.$alert('您没有此权限，即将返回首页。', '提示', {
          confirmButtonText: '确定',
          callback: action => {
            this.$router.push('/home');
          }
        });
        return
      }
      else{
        this.$axios.get(`http://127.0.0.1:5000/userInfo`).then((res)=>{
          console.log(res);
          this.tableData = res.data;
          this.total = this.tableData.length;
          console.log(res.data);
        });
      }
    });
  },
  methods: {
    current_change: function(currentPage){
      this.currentPage = currentPage;
    },
    async vague() {
      this.$axios.post(`http://127.0.0.1:5000/userVagueSelect`, this.words).then((res)=>{
        console.log(res);
        this.tableData = res.data;
        this.total  = this.tableData.length;
        console.log(res.data);
      });
    },
    handleEdit(row) {
      this.$axios.post(`http://127.0.0.1:5000/initPassword`, row).then((res)=>{
        if (res.data == 1){
          window.location.reload();
        }
        else {
          this.$message({
            showClose: true,
            message: '修改失败，请核对后重新尝试',
            type: 'info'
          });
        }
      });
    }
  }
}
</script>

<style>

.menu{
  width: 100%;
  float: left;
  height: 673px;
}
.main{
  width: 1800px;
}
.bodyDiv{
  width: 100%;
  display: flex;
}
.menu{
  width: 100%;
  float: left;
}
.demo-table-expand {
  font-size: 0;
}
.demo-table-expand label {
  width: 90px;
  color: #99a9bf;
}
.demo-table-expand .el-form-item {
  margin-right: 0;
  margin-bottom: 0;
  width: 50%;
}

</style>

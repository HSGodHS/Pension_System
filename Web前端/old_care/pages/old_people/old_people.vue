<template>
  <el-container direction="vertical">

    <navMenu width="100%"></navMenu>

    <el-container direction="horizontal">
      <el-aside width="280px" height="100%">
        <sideBar class="menu" page-index="3" open-index="0" ></sideBar>
      </el-aside>
      <el-main>

        <el-container direction="horizontal">
          <el-input v-model="words.word" placeholder="请输入检索风险名称（支持模糊查询）"></el-input>
          <el-button style="margin-left: 20px" @click="vague()">搜索</el-button>
          <el-button @click="openDrawer" type="primary" >添加</el-button>
        </el-container>

        <el-table
          :data="tableData.slice((currentPage-1)*pagesize,currentPage*pagesize)"
          height="502"
          style="width: 100%; margin-top: 20px">

          <el-table-column
            prop="risk_id"
            label="风险编号">
          </el-table-column>
          <el-table-column
            prop="name"
            label="风险名称">
          </el-table-column>
          <el-table-column
            prop="component_name"
            label="具体组分名称">
          </el-table-column>

          <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button
                size="small"
                @click="showDetail(scope.row)">
                更多信息
                <i class="el-icon-s-order"></i>
              </el-button>
            </template>
          </el-table-column>

        </el-table>

        <div style="text-align: center;margin-top: 20px;">
          <el-pagination
            background
            layout="prev, pager, next"
            :page-size="pagesize"
            :total="total"
            @current-change="current_change">
          </el-pagination>
        </div>

        <el-drawer
          size="35%"
          title="新增数据"
          :visible.sync="drawer"
          :direction="direction"
          :before-close="handleClose">
          <el-container>
            <el-main>
              <p style="margin-left: 30px; margin-top: 20px; font-size: 16px">风险名称</p>
              <el-input v-model="newData.name" style="margin-top: 12px"></el-input>
              <p style="margin-left: 30px; margin-top: 20px; font-size: 16px">组分名称</p>
              <el-select v-model="newData.cpnt_name" placeholder="请选择" style="margin-top: 12px; width: 100%" @change="cpntShow">
                <el-option
                  v-for="item in options"
                  :value="item.component_names">
                </el-option>
              </el-select>
              <p style="margin-left: 30px; margin-top: 20px; font-size: 16px">车辆编号: {{cpntData.train}}</p>
              <p style="margin-left: 30px; margin-top: 20px; font-size: 16px">站点名称: {{cpntData.station}}</p>
              <p style="margin-left: 30px; margin-top: 20px; font-size: 16px">里程标名称: {{cpntData.mileMark}}</p>

            </el-main>
          </el-container>
          <el-button style="margin-top: 10px; margin-left: 390px" @click="submit" type="primary">确&nbsp;&nbsp;&nbsp;&nbsp;认</el-button>
        </el-drawer>

      </el-main>
    </el-container>
  </el-container>

</template>

<script>
import sideBar from "~/components/sideBar";
import navMenu from "~/components/navMenu";
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
    this.$axios.get(`http://127.0.0.1:5000/riskinfo`).then((res)=>{
      console.log(res);
      this.tableData = res.data;
      this.total = this.tableData.length;
      console.log(res.data);
    });
  },
  methods: {
    current_change: function(currentPage){
      this.currentPage = currentPage;
    },
    async vague() {
      this.$axios.post(`http://127.0.0.1:5000/riskVagueSelect`, this.words).then((res)=>{
        console.log(res);
        this.tableData = res.data;
        this.total  = this.tableData.length + 3;
        console.log(res.data);
      });
    },
    handleClose(done) {
      this.$confirm('确认关闭？')
        .then(_ => {
          done();
          console.log("我关了哦");
          this.newData.name = '';
          this.newData.cpnt_name = '';
        })
        .catch(_ => {});
    },
    async openDrawer() {
      this.$axios.get(`http://127.0.0.1:5000/cpntname`).then((res)=>{
        console.log(res.data);
        this.options = res.data;
      });
      this.drawer = true;
      console.log(this.options)
    },
    showDetail(row) {
      console.log(row)
      this.$router.push({name:'risk-detail',query:{risk_id: row.risk_id}})
    },
    submit() {
      this.$axios.post(`http://127.0.0.1:5000/addRisk`, this.newData).then((res)=>{
        console.log(res);
        if (res.data==1){
          window.location.reload();
        }
        else {
          this.$message('信息输入有误或已存在！')
        }

      });

    },
    cpntShow(vId) {
      this.$axios.post(`http://127.0.0.1:5000/cpntData`, {cpntName: vId}).then((res)=>{
        this.cpntData = res.data;
        console.log(res);

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

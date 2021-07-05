<template>
  <el-container direction="vertical">

    <navMenu width="100%"></navMenu>

    <el-container direction="horizontal" >
      <el-aside width="280px" height="100%">
        <sideBar class="menu" page-index="3" open-index="0" style="height: 100%"></sideBar>
      </el-aside>
      <el-main>

        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span style="font-size: 20px">风险信息</span>
            <el-button style="float: right; padding: 3px 0" type="text" @click="openDrawer1">编辑</el-button>
            <el-button style="float: right; padding: 3px 10px" type="text" @click="DeleteRisk">失效</el-button>
          </div>
          <div class="mg">
            <p>风险项名称：&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{riskinfo.risk_name}}</p>
            <p>风险所属组分：&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{riskinfo.cpnt_name}}</p>
            <p>风险描述：&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{riskinfo.describe}}</p>
          </div>
        </el-card>

        <el-card class="box-card" style="margin-top: 20px">
          <div slot="header" class="clearfix">
            <span style="font-size: 20px">风险点核查规则</span>
            <el-button style="float: right; padding: 3px 0" type="text" @click="openDrawer2">编辑</el-button>
          </div>
          <div class="mg">
            <p>监测间隔：&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{riskinfo.gap}}</p>
            <p>开始结束时间：&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{riskinfo.time1}} -- {{riskinfo.time2}}</p>
          </div>
        </el-card>

<!--        风险点阈值-->
        <el-card class="box-card" style="margin-top: 20px">
          <div slot="header" class="clearfix">
            <span style="font-size: 20px">风险点阈值及处置规范</span>
            <el-button style="float: right; padding: 3px 0" type="text" @click="openDrawer3">新增</el-button>
          </div>
          <div class="mg">
            <el-table
              :data="theData"
              height="420"
              style="width: 100%">

              <el-table-column type="expand">
                <template slot-scope="props">
                  <el-form label-position="left" inline class="demo-table-expand">
                    <el-form-item label="阈值属性">
                      <span>{{ props.row.attribute}}</span>
                    </el-form-item>
                    <el-form-item label="判定条件">
                      <span>{{ props.row.range}}</span>
                    </el-form-item>
                    <el-form-item label="具体阈值">
                      <span>{{ props.row.norm}}</span>
                    </el-form-item>
                    <el-form-item label="危险程度">
                      <span>{{ props.row.level}}</span>
                    </el-form-item>
                    <el-form-item label="应对措施">
                      <span>{{ props.row.method}}</span>
                    </el-form-item>
                  </el-form>
                </template>
              </el-table-column>

              <el-table-column
                prop="threshold_id"
                label="阈值编号">
              </el-table-column>
              <el-table-column
                prop="attribute"
                label="阈值属性">
              </el-table-column>
              <el-table-column
                prop="range"
                label="判定条件">
              </el-table-column>
              <el-table-column
                prop="norm"
                label="具体阈值">
              </el-table-column>
              <el-table-column
                prop="level"
                label="危险程度">
              </el-table-column>

              <el-table-column label="操作">
                <template slot-scope="scope">
                  <el-button
                    icon="el-icon-edit"
                    circle
                    size="small"
                    @click="openDrawer5(scope.row)">
                  </el-button>
                  <el-button icon="el-icon-delete" circle size="small"
                             @click="handleDelete(scope.row)"></el-button>
                </template>
              </el-table-column>

            </el-table>
          </div>
        </el-card>

<!--        风险点记录-->
        <el-card class="box-card" style="margin-top: 20px">
          <div slot="header" class="clearfix">
            <span style="font-size: 20px">风险监测记录</span>
            <el-button style="float: right; padding: 3px 0" type="text" @click="openDrawer4">新增</el-button>
          </div>
          <div class="mg">
            <el-table
              :data="theRecord"
              height="300"
              style="width: 100%">

              <el-table-column
                prop="record_id"
                label="风险记录编号">
              </el-table-column>
              <el-table-column
                prop="record_norm"
                label="监测值">
              </el-table-column>

              <el-table-column
                prop="record_result"
                label="监测结果"
                :filters="[{ text: '正常', value: '正常' }, { text: '存在风险', value: '存在风险' },
                           { text: '较大风险', value: '较大风险' }, { text: '重大风险', value: '重大风险' }]"
                :filter-method="filterTag"
                filter-placement="bottom-end">
                <template slot-scope="scope">
                  <el-tag
                    :type="scope.row.record_result === '正常' ? 'success' : (scope.row.record_result === '存在风险' ? 'primary' :
                    (scope.row.record_result === '较大风险' ? 'warning' : 'danger'))"
                    disable-transitions>{{scope.row.record_result}}</el-tag>
                </template>
              </el-table-column>

              <el-table-column
                prop="record_time"
                label="监测时间">
              </el-table-column>
              <el-table-column
                prop="record_staff_id"
                label="监测员工">
              </el-table-column>

            </el-table>
          </div>
        </el-card>
        <el-backtop>
          <i class="el-icon-caret-top"></i>
        </el-backtop>

<!--        风险信息修改-->
        <el-drawer
          size="35%"
          title="修改风险信息"
          :visible.sync="drawer1"
          :direction="direction"
          :before-close="handleClose">
          <el-container>
            <el-main>
              <p style="margin-left: 10px; font-size: 18px">风险名称</p>
              <el-input v-model="deliverParam.name" style="margin-top: 20px"></el-input>
              <p style="margin-left: 10px; margin-top:20px; font-size: 18px">组分名称</p>
              <el-select v-model="deliverParam.cpnt_name" placeholder="请选择" style="margin-top: 20px; width: 100%" ><p style="margin-left: 10px; font-size: 18px">组分名称</p>
                <el-option
                  v-for="item in options"
                  :value="item.component_names">
                </el-option>
              </el-select>
              <p style="margin-left: 10px; font-size: 18px; margin-top:20px; ">风险描述</p>
              <el-input
                type="textarea"
                :rows="10"
                placeholder="简要描述风险的特征，字数不超300字。"
                v-model="deliverParam.describe"
                style="margin-left: 5px; margin-top: 20px; width: 100%"></el-input>

            </el-main>
          </el-container>
          <el-button style="margin-top: 10px; margin-left: 390px" @click="submit1" type="primary">确&nbsp;&nbsp;&nbsp;&nbsp;认</el-button>
        </el-drawer>

<!--        风险核查时间修改-->
        <el-drawer
          size="35%"
          title="修改核查规则"
          :visible.sync="drawer2"
          :direction="direction"
          :before-close="handleClose">
          <el-container>
            <el-main>
              <p style="margin-left: 10px; font-size: 18px">核查时间间隔</p>
              <el-input v-model="deliverParam.gap" style="margin-top: 20px"></el-input>
              <p style="margin-left: 10px; margin-top:20px; font-size: 18px">开始结束时间</p>

              <el-date-picker
                v-model="deliverParam.time"
                type="daterange"
                range-separator="至"
                start-placeholder="开始日期"
                end-placeholder="结束日期"
                style="width: 100%; margin-top: 20px">
              </el-date-picker>

            </el-main>
          </el-container>
          <el-button style="margin-top: 10px; margin-left: 390px" @click="submit2" type="primary">确&nbsp;&nbsp;&nbsp;&nbsp;认</el-button>
        </el-drawer>

<!--        新增风险阈值-->
        <el-drawer
          size="35%"
          title="新增风险阈值"
          :visible.sync="drawer3"
          :direction="direction"
          :before-close="handleClose">
          <el-container>
            <el-main>
              <p style="margin-left: 10px; margin-top: 10px; font-size: 18px">阈值属性</p>
              <el-input v-model="deliverParam.attribute" style="margin-top: 10px"></el-input>
              <p style="margin-left: 10px; margin-top: 10px; font-size: 18px">判定条件</p>
              <el-select v-model="deliverParam.range" placeholder="请选择" style="margin-top: 12px; width: 100%" >
                <el-option v-for="item in rrange" :value="item.value"></el-option>
              </el-select>
              <p style="margin-left: 10px; margin-top: 10px; font-size: 18px">具体阈值</p>
              <el-input v-model="deliverParam.norm" style="margin-top: 10px"></el-input>
              <p style="margin-left: 10px; margin-top: 10px; font-size: 18px">危险程度</p>
              <el-select v-model="deliverParam.level" placeholder="请选择" style="margin-top: 12px; width: 100%" >
                <el-option v-for="item in lerange" :value="item.value"></el-option>
              </el-select>
              <p style="margin-left: 10px; margin-top: 10px; font-size: 18px">应对措施</p>
              <el-input
                type="textarea"
                :rows="5"
                placeholder="简要描述风险的特征以及处理方法，字数不超300字。"
                v-model="deliverParam.method"
                style="margin-left: 5px; margin-top: 10px; width: 100%"></el-input>

            </el-main>
          </el-container>
          <el-button style="margin-top: 10px; margin-left: 390px" @click="submit3" type="primary">确&nbsp;&nbsp;&nbsp;&nbsp;认</el-button>
        </el-drawer>

<!--        修改风险阈值-->
        <el-drawer
          size="35%"
          title="修改风险阈值"
          :visible.sync="drawer5"
          :direction="direction"
          :before-close="handleClose">
          <el-container>
            <el-main>
              <p style="margin-left: 10px; margin-top: 10px; font-size: 18px">判定条件</p>
              <el-select v-model="deliverParam.range" placeholder="请选择" style="margin-top: 12px; width: 100%" >
                <el-option v-for="item in rrange" :value="item.value"></el-option>
              </el-select>
              <p style="margin-left: 10px; margin-top: 10px; font-size: 18px">具体阈值</p>
              <el-input v-model="deliverParam.norm" style="margin-top: 10px"></el-input>
              <p style="margin-left: 10px; margin-top: 10px; font-size: 18px">危险程度</p>
              <el-select v-model="deliverParam.level" placeholder="请选择" style="margin-top: 12px; width: 100%" >
                <el-option v-for="item in lerange" :value="item.value"></el-option>
              </el-select>
              <p style="margin-left: 10px; margin-top: 10px; font-size: 18px">应对措施</p>
              <el-input
                type="textarea"
                :rows="5"
                placeholder="简要描述风险的特征以及处理方法，字数不超300字。"
                v-model="deliverParam.method"
                style="margin-left: 5px; margin-top: 10px; width: 100%"></el-input>

            </el-main>
          </el-container>
          <el-button style="margin-top: 10px; margin-left: 390px" @click="submit5" type="primary">确&nbsp;&nbsp;&nbsp;&nbsp;认</el-button>
        </el-drawer>

<!--        新增风险记录-->
        <el-drawer
          size="35%"
          title="新增风险监测记录"
          :visible.sync="drawer4"
          :direction="direction"
          :before-close="handleClose">
          <el-container>
            <el-main>
              <p style="margin-left: 10px; font-size: 18px">监测值</p>
              <el-input v-model="deliverParam.record_norm" style="margin-top: 20px"></el-input>

            </el-main>
          </el-container>
          <el-button style="margin-top: 10px; margin-left: 390px" @click="submit4" type="primary">确&nbsp;&nbsp;&nbsp;&nbsp;认</el-button>
        </el-drawer>


      </el-main>
    </el-container>
  </el-container>


</template>

<script>
import sideBar from "@/components/sideBar";
import navMenu from "@/components/navMenu";
export default {
  name: "detail",
  components: {sideBar, navMenu},

  data() {
    return {
      riskinfo: {
          risk_name: '',
          cpnt_name: '',
          describe: '',
          gap: '',
          time1: '',
          time2: '',
      },
      deliverParam: {
        name: '',
        describe: '',
        cpnt_name: '',
        id: '',
        gap: '',
        time: '',
        range: '',
        norm: '',
        method: '',
        attribute: '',
        level: '',
        record_norm: '',
        threshold_id: '',
      },
      theData: [],
      theRecord: [],
      words: {
        word: ''
      },
      drawer1: false,//修改详细信息
      drawer2: false,//修改核查规则
      drawer3: false,//新增阈值
      drawer4: false,//新增核查记录
      drawer5: false,//修改阈值
      direction: 'rtl',
      newData: {
        name: '',
        cpnt_name: '',
      },
      options: [{
        component_names: ''
      }],
      rrange: [
        {value: '小于'},
        {value: '大于'},
        {value: '不等于'}
      ],
      lerange: [
        {value: '低'},
        {value: '中'},
        {value: '高'}
      ],
    }
  },
  mounted() {
    this.deliverParam.id = this.$route.query.risk_id;
    this.$axios.post(`http://127.0.0.1:5000/selectDetail`, this.deliverParam).then((res)=>{
      console.log(res.data);
      this.riskinfo = res.data[0];
    });
    this.$axios.post(`http://127.0.0.1:5000/selectThreshold`, this.deliverParam).then((res)=>{
      console.log(res.data);
      this.theData = res.data;
    });
    this.$axios.post(`http://127.0.0.1:5000/selectRecord`, this.deliverParam).then((res)=>{
      console.log(res.data);
      this.theRecord = res.data;
    });

  },
  methods: {
    current_change: function(currentPage){
      this.currentPage = currentPage;
    },
    handleClose(done) {
      this.$confirm('确认关闭？')
        .then(_ => {
          done();
          this.deliverParam.describe = '';
          this.deliverParam.name = '';
          this.deliverParam.cpnt_name = '';
          this.deliverParam.gap = '';
          this.deliverParam.time = '';
          this.deliverParam.record_norm = '';
          this.deliverParam.range = '';
          this.deliverParam.level = '';
          this.deliverParam.method = '';
          this.deliverParam.norm = '';
          this.deliverParam.attribute = '';
        })
        .catch(_ => {});
    },
    resetDateFilter() {
      this.$refs.filterTable.clearFilter('date');
    },
    clearFilter() {
      this.$refs.filterTable.clearFilter();
    },
    formatter(row, column) {
      return row.address;
    },
    filterTag(value, row) {
      return row.record_result === value;
    },
    filterHandler(value, row, column) {
      const property = column['property'];
      return row[property] === value;
    },
    async openDrawer1() {
      this.$axios.get(`http://127.0.0.1:5000/cpntname`).then((res)=>{
        console.log(res.data);
        this.options = res.data;
      });
      this.drawer1 = true;
    },
    async openDrawer2() {
      this.$axios.get(`http://127.0.0.1:5000/cpntname`).then((res)=>{
        console.log(res.data);
        this.options = res.data;
      });
      this.drawer2 = true;
    },
    async openDrawer3() {
      this.drawer3 = true;
    },
    async openDrawer4() {
      this.drawer4 = true;
    },
    async openDrawer5(row) {
      this.deliverParam.threshold_id = row.threshold_id
      this.drawer5 = true;
    },
    handleDelete(row) {

      this.$confirm('此操作将永久删除该记录, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.onDelete(row);
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        });
      });
    },
    DeleteRisk() {
      this.$confirm('此操作将永久删除该记录, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
          this.$axios.post(`http://127.0.0.1:5000/DelRisk`, this.deliverParam).then((res)=>{
            if (res.data==1){
              this.$router.push('/risk/risk');
            }
            else {
              this.$message('删除失败，请检查其余部分')
            }
          });
      }).catch(() => {
            this.$message({
              type: 'info',
              message: '已取消删除'
            });
      });
    },
    onDelete(row) {
      this.$axios.post(`http://127.0.0.1:5000/deleteThreshold`, row).then((res)=>{

        window.location.reload();
      });
    },
    // 提交的是对风险详细信息的修改
    submit1() {
      if (this.deliverParam.name == '' || this.deliverParam.describe == '' || this.deliverParam.cpnt_name == '') {
        this.$message('信息输入有误请核对后再次提交');
        return;
      }
      this.$axios.post(`http://127.0.0.1:5000/modifyDetail`, this.deliverParam).then((res)=>{
        if (res.data==1){
          window.location.reload();
        }
        else {
          this.$message('信息输入有误或已存在！')
        }
      });
    },
    // 提交的是对核查规则的修改
    submit2() {
      console.log(this.deliverParam);
      this.$axios.post(`http://127.0.0.1:5000/modifyGap`, this.deliverParam).then((res)=>{
        if (res.data==1){
          window.location.reload();
        }
        else {
          this.$message('信息输入有误或已存在！')
        }
      });
    },
    // 提交的是新增阈值 有问题
    submit3() {
      if (this.deliverParam.range == '' || this.deliverParam.norm == '' || this.deliverParam.method == '' || this.deliverParam.level == '') {
        this.$message('信息输入有误请核对后再次提交');
        return;
      }
      this.$axios.post(`http://127.0.0.1:5000/addThd`, this.deliverParam).then((res)=>{
        if (res.data==1){
          window.location.reload();
        }
        else {
          this.$message('信息输入有误或已存在！')
        }
      });
    },
    //提交的是新增核查记录
    submit4() {
      if (this.deliverParam.record_norm == '') {
        this.$message('信息输入有误请核对后再次提交');
        return;
      }
      this.$axios.post(`http://127.0.0.1:5000/addRecord`, this.deliverParam).then((res)=>{
        if (res.data==1){
          window.location.reload();
        }
        else {
          this.$message('信息输入有误或已存在！')
        }
      });
    },
    // 提交的是对已有阈值的修改
    submit5() {
      if (this.deliverParam.range == '' || this.deliverParam.norm == '' || this.deliverParam.level == '' || this.deliverParam.method == '' ){
        this.$message('信息输入有误请核对后再次提交');
        return;
      }
      this.$axios.post(`http://127.0.0.1:5000/modifyThreshold`, this.deliverParam).then((res)=>{
        if (res.data==1){
          window.location.reload();
        }
        else {
          this.$message('信息输入有误或已存在！')
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
.mg{
  line-height: 40px;
  font-size: 17px;
}

</style>

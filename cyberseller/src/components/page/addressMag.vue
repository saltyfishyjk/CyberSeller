<template>
  <div style="height: 100%;">
    <!--    地址-->
    <div style="width: 90%;margin-left: 10%;margin-top: 50px;">
      <h1 style="font-size: 23px;color: #c91623;">收货地址管理</h1>
      <div style="width: 23%;float: left;margin-left: 20px;margin-bottom: 10px;"
           v-for="(item, index) in userAddress"
           @click="setFirst(index)">
        <!--          地址卡片-->
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <span>{{ item.default ==1?"默认地址":"备用地址"}}</span>

            <!--              设置默认按钮-->
            <el-button style="float: right; padding: 3px 0"
                       type="text"
                       v-show="item.default ==1?false:true"
                       @click="setDefault(item)">
              设置为默认
            </el-button>
            <!--              删除按钮-->
            <el-button style="float: right; padding: 3px 0"
                       type="text"
                       v-show="item.default ==1?false:true"
                       @click="deleteAddr(item)">
              删除地址   |
            </el-button>

          </div>
          <p>{{ item.receiver_name }}</p>
          <p>{{ item.phone }}</p>
          <p>{{ item.addr }}</p>
          <p>{{ item.detailed_addr }}</p>
        </el-card>
      </div>
<!--      添加按钮  -->


      <button class="addbtn2" @click="addVis=!addVis">
        添加
      </button>
<!--      <div class="addbtn"-->
<!--           :style="seen==0?'background: #00a854;':'background: #4D6530;'"-->
<!--           @mouseenter="enter()"-->
<!--           @mouseleave="leave()"-->
<!--            @click="addVis=!addVis">-->
<!--        <div style="background: black;width: 8%;height: 35%;margin-left: 46%;margin-top: 18%;border-radius: 5px;">-->

<!--        </div>-->
<!--        <div style="background: black;width: 70%;height: 8%;margin-left: 15%;margin-top: -5%;border-radius: 5px;">-->

<!--        </div>-->
<!--        <div style="background: black;width: 8%;height: 35%;margin-left: 46%;margin-top: -5%;border-radius: 5px;">-->

<!--        </div>-->

<!--      </div>-->


    </div>

    <!-- 弹出添加框 -->
    <el-dialog title="添加地址" :visible.sync="addVis" width="30%">
      <el-form ref="form" :model="form"  :rules="rules" label-width="95px">
        <el-form-item label="收件人" prop="reseP"><el-input v-model="form.reseP"></el-input></el-form-item>
        <el-form-item label="联系电话" prop="tel"><el-input v-model="form.tel"></el-input></el-form-item>
        <el-form-item label="地址" prop="address"><el-input v-model="form.address"></el-input></el-form-item>
        <el-form-item label="详细地址" prop="address2"><el-input v-model="form.address2"></el-input></el-form-item>
        <el-form-item label="备注"><el-input v-model="form.desc"></el-input></el-form-item>
      </el-form>

      <span slot="footer" class="dialog-footer">
                <el-button @click="addVis = false">取 消</el-button>
                <el-button @click="resetForm('form')">重 置</el-button>
                <el-button type="primary" @click="saveAdd('form')">确 定</el-button>
            </span>
    </el-dialog>

  </div>
</template>

<script>
import { postForm } from "@/api";
export default {
  inject: ['reload'],
        name: "addressMag",
      data()
      {
        let tmp_user_addrs=this.loadAddrData()
        return {
          seen: 0,
          addVis: false,
          form: {},
          //数据
          userAddress: tmp_user_addrs,
          //验证规则
          rules: {
            reseP: [
              { required: true, message: '请输入收件人', trigger: 'blur' },
              { min: 1, max: 10, message: '长度在 1 到 10 个字符', trigger: 'blur' }
            ],
            tel: [
              { required: true, message: '请输入联系电话', trigger: 'blur' },
              { min: 11, max: 11, message: '', trigger: 'blur' }
            ],
            address: [
              { required: true, message: '请选择地址', trigger: 'change' }
            ],
            address2: [
              { required: true, message: '请输入详细地址', trigger: 'blur' },
              { min: 3, max: 30, message: '长度在 3 到 30 个字符', trigger: 'blur' }
            ]
          },
          
        }},
      created() {
      },
  methods: {
        setDefault(item) {
          console.log(item)
          let fd = new FormData()
          fd.append('address_id', item.address_id)
          fd.append('default', 1)
          console.log(item.address_id)
          postForm(`http://43.143.179.158:8080/updateDefaultAddress`, fd).then(res => {
            console.log(res)
          })
          .catch(function (error) {
            console.log(error)
          });
          this.loadAddrData()
          this.reload()
        },
        deleteAddr(item) {
          console.log(item)
          let fd = new FormData()
          fd.append('address_id', item.address_id)
          console.log(item.address_id)
          postForm(`http://43.143.179.158:8080/deleteAddress`, fd).then(res => {
            console.log(res)
          })
          .catch(function (error) {
            console.log(error)
          });
          this.loadAddrData()
          this.reload();
        },
        loadAddrData() {
          console.log('initialize data in')
          let fd = new FormData()
          fd.append('user_id', localStorage.getItem('userId'))
          postForm(`http://43.143.179.158:8080/getAddress`, fd).then(res => {
            console.log(res)
            this.userAddress = res.addresses
          })
          .catch(function (error) {
            console.log(error)
          });
        },
        setFirst(index)
        {
          const length = this.userAddress.length;
          for (let i = 0; i < length; i++) {
            this.userAddress[i].default = 2;
          }
          this.userAddress[index].default = 1;
        },enter(){
          this.seen = 1;
        },
        leave(){
          this.seen = 0;
        },
        // 保存添加
        saveAdd(formName) {
          
          let fd = new FormData()
          fd.append('receiver_name', this.form.reseP)
          fd.append('phone', this.form.tel)
          fd.append('addr', this.form.address)
          fd.append('detailed_addr', this.form.address2)
          if (this.form.desc!=null) {
            fd.append('comment', this.form.desc)
          }
          fd.append('default', 0)
          fd.append('user_id', localStorage.getItem('userId'))
          postForm(`http://43.143.179.158:8080/addAddress`, fd).then(res => {
            if (res.succeed) {
              this.$message.success('添加成功');
              this.addVis = false;
            } else {
              console.log('error submit!!');
              return false;
            }
          })
            .catch(function (error) {
              console.log(error)
            });
          this.reload();
        },
        resetForm(formName) {
          this.$refs[formName].resetFields();
        }
      }
    }
</script>

<style scoped>
.addbtn{
  /*background: cyan;*/
  width: 80px;
  /*background: #00a854;*/
  /*background: #4D6530;*/
  height: 80px;
  text-align: center;
  float: left;
  border-radius: 100px;
  margin-left: 20px;
}
.addbtn2{
    height: 100px;
    margin-left: 30px;
    width: 100px;
    background-color: #428bca;
    border-color: #357ebd;
    color: #fff;
    -moz-border-radius: 15px;
    -webkit-border-radius: 15px;
    text-align: center;
    vertical-align: middle;
    font-weight: 900;
    font-size:125%
  }
</style>

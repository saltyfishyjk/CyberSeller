<template>
    <div class="title" style="width: 65%;margin-left: 20%;">
      <h3 v-once v-if="getSellData()">我的订单</h3>
      <el-table :data="tableData.filter(data => !search || data.name.toLowerCase().includes(search.toLowerCase()))"
        style="width: 100%;">
    
        <el-table-column label="商品" prop="picture" width="110px" align="center">
          <template slot-scope="scope">
            <el-image style="width: 100px; height: 100px;" :src="scope.row.picture" />
          </template>
        </el-table-column>
        <el-table-column label="商品名" prop="name" align="center"></el-table-column>
        <el-table-column label="卖家" prop="seller_name" align="center"></el-table-column>
        <el-table-column label="单价" prop="prize" width="110px" align="center">
          <template slot-scope="scope">
            <span>&yen;</span>{{ scope.row.price }}
          </template>
        </el-table-column>
      </el-table>
    </div>
</template>
<script>
import { postForm } from "@/api";
export default {
  inject: ['reload'],
  name: "goodsInfo",
  data() {
    return {
      tableData: null,
      init_sell_data: true,
      search: '',
      good_id: '',
      //选中列表
      multipleSelection: [],
      chooseList: [],
      editable: true,
      ruleForm: {
        name: '',
        image: null,
        price: '',
        maker: '',
        description: '',
        date: '',
        shelf_life: '',
        others: null
      },
      rules: {
        name: [
          { required: true, message: '请输入商品名称', trigger: 'blur' },
        ],
        image: [
          { required: true, message: '请上传图片', trigger: 'blur' },
        ],
        price: [
          { required: true, message: '请输入商品价格', trigger: 'blur' },
        ],
        maker: [
          { required: false, message: '请输入制造商', trigger: 'blur' },
        ],
        description: [
          { required: false, message: '请输入商品描述信息', trigger: 'blur' },
        ],
        date: [
          { required: false, message: '请输入生产日期', trigger: 'blur' },
        ],
        shelf_life: [
          { required: false, message: '请输入保质期', trigger: 'blur' },
        ],
      }
    }
  },
  methods: {
    submitForm(formName) {
      let fd = new FormData()
      fd.append('name', this.ruleForm.name)
      fd.append('price', this.ruleForm.price)
      fd.append('picture', this.ruleForm.image)
      fd.append('seller_id', localStorage.getItem('userId'))
      if (this.ruleForm.maker != '') {
        fd.append('maker', this.ruleForm.maker)
      }
      if (this.ruleForm.description != '') {
        fd.append('description', this.ruleForm.description)
      }
      if (this.ruleForm.date != '') {
        fd.append('date', this.ruleForm.date)
      }
      if (this.ruleForm.shelf_life != '') {
        fd.append('shelf_life', this.ruleForm.shelf_life)
      }
      console.log(typeof this.ruleForm.name)
      console.log(typeof this.ruleForm.price)
      console.log(this.ruleForm.price)
      console.log(localStorage.getItem('userId'))
      postForm(`http://43.143.179.158:8080/addGoods`, fd).then(res => {
        console.log(res)
        this.getSellData()
        this.reload()
        this.good_id = res.good_id
      })
        .catch(function (error) {
          console.log(error);
        });
      if (this.ruleForm.others != null) {
        console.log(this.ruleForm.others)
        let excel_file = new FormData()
        excel_file.append('excel', this.ruleForm.others)
        excel_file.append('good_id', this.good_id)
        postForm(`http://43.143.179.158:8080/analyseExcel`, excel_file).then(res => {
          console.log(res)
        })
          .catch(function (error) {
            console.log(error);
          });
      }
    },
    getImageFile: function (e) {
      console.log(this.$refs["img"].files);
      console.log(this.$refs["img"].files[0]);
      if (this.$refs["img"].files[0]) {
        this.ruleForm.image = this.$refs["img"].files[0];
      } else {
        this.ruleForm.image = null;
      }
      console.log('上传类型')
      console.log(typeof this.ruleForm.image)
    },
    getExcelFile: function (e) {
      console.log(this.$refs["file"].files);
      console.log(this.$refs["file"].files[0]);
      if (this.$refs["file"].files[0]) {
        this.ruleForm.others = this.$refs["file"].files[0];
      } else {
        this.ruleForm.others = null;
      }
      console.log('上传类型')
      console.log(typeof this.ruleForm.others)
    },
    resetForm(formName) {
      this.$refs.ruleForm.resetFields()
      this.ruleForm.image = null;
    },
    canSelect(row) {
      if (row.status == 1)
        return false;
      else return true;
    },
    handleEdit(row) {
      let repo_goods_id = row.id
      console.log(row.repo)
      let fd = new FormData()
      fd.append('repo', row.repo)
      fd.append('good_id', repo_goods_id)
      postForm(`http://43.143.179.158:8080/updateRepo`, fd).then(res => {
        if (res.succeed) {
          this.init_sell_data = true
        }
      })
        .catch(function (error) {
        });
      if (this.tableData == null) {
        return false
      }
    },
    handleDelete(row) {
      let repo_goods_id = row.id
      console.log('delete ' + row.id)
      let fd = new FormData()
      fd.append('good_id', repo_goods_id)
      postForm(`http://43.143.179.158:8080/deleteGood`, fd).then(res => {
        if (res.succeed) {
          this.init_sell_data = true
        }
      })
        .catch(function (error) {
        });
      if (this.tableData == null) {
        return false
      }
    }
    ,
    goodsStatus(status) {
      if (status == "1")
        return "danger";
      else if (status == "2")
        return "";
    },
    getSellData() {
      if (!this.init_sell_data) {
        return true
      }
      this.init_sell_data = false
      let fd = new FormData()
      fd.append('user_id', localStorage.getItem('userId'))
      console.log('Call Database for SellData')
      postForm(`http://43.143.179.158:8080/mainRecommendGoods`, fd).then(res => {
        this.tableData = res.goods
      })
        .catch(function (error) {
          console.log(error)
        });
      return true
    }
  }
}
</script>

<style scoped>
.avatar {
  width: 100px;
  height: 100px;
}

.el-upload {
  width: 100px;
  height: 100px;
  line-height: 100px;
  margin-left: 60px;
}

.new_goods {
  position: absolute;
  top: 20%;
  left: 1%;
  width: 75%;
  height: 75%;
  /*background-color: #409EFF;*/
  /*text-align: center; */
  /* vertical-align: middle; */
}


.title {
  margin-top: 50px;
}

.title h3 {
  /*float: left;*/
  font-size: 23px;
  color: #c91623;
  margin-bottom: 30px;
}

/*商品结算*/
.balance {
  height: 50px;
  margin-top: 40px;
}

.balance li {
  float: left;
  line-height: 5px;
  margin-left: 22px;
}

.balance_ul2 {
  float: right;
  margin-right: 10px;
}

.balance_ul1 .button1 {
  margin-top: 5px;
}

.balance_ul2 .spanText {
  font-size: 25px;
  color: #C91623;
  font-weight: bold;
}

.balance_ul2 button {
  width: 100px;
  height: 50px;
  background-color: brown;
  border: 1px solid #c91623;
  font-weight: bold;
  font-size: 20px;
  color: white;
}

.balance_ul2 button:hover {
  background-color: #C91623;
}
</style>

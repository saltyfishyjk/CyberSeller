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
    resetForm(formName) {
      this.$refs.ruleForm.resetFields()
      this.ruleForm.image = null;
    },
    canSelect(row) {
      if (row.status == 1)
        return false;
      else return true;
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
      postForm(`http://43.143.179.158:8080/getSale`, fd).then(res => {
        console.log(res)
        var ans = []
        for (var i = 0; i < res.sales.length; i++) {
          var json_e = res.sales[i]
          console.log(json_e)
          for (var row = 0; row < json_e.length; row++) {
            var ele = json_e[row]
            console.log(ele)
            ans.push(ele)
          }
        }
        this.tableData = ans
        console.log(this.tableData)
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

<template>
  <div>
    <!--表头-->
    <div class="title" style="width: 80%;margin-left: 10%;">
      <h3>收藏</h3>
      <el-table
        ref="multipleTable"
        @row-click="goDesc"
        :data="tableData.filter(data => !search || data.name.toLowerCase().includes(search.toLowerCase()))"
        style="width: 100%;">
<!--        商品图片-->
        <el-table-column label="商品" prop="img" width="110px" align="center">
          <template slot-scope="scope">
            <el-image style="width: 100px; height: 100px;" :src="scope.row.picture"/>
          </template>
        </el-table-column>
        <!--        商品名字-->
        <el-table-column label="商品名" prop="name" align="center"></el-table-column>
        <!--        商品单价-->
        <el-table-column label="单价"  prop="prize" width="110px" align="center">
          <template slot-scope="scope">
            <span>&yen;</span>{{scope.row.price}}
          </template>
        </el-table-column>
        <!--        上下架状态-->
        <el-table-column label="状态"  prop="prize" width="110px" align="center">
          <template slot-scope="scope">
            <el-tag :type="goodsStatus(scope.row.repo)">{{"在售"}}</el-tag>
          </template>
        </el-table-column>
      </el-table>
    </div>
    <div style="width: 80%;margin-left: 10%;">

    </div>
  </div>
</template>

<script>
  import { postForm } from '../../api';
  export default {
    name: "collection",
    data()
    {
      return{
        tableData: null,
        search : '',
      }
    },
    created() {
      let fd = new FormData()
      fd.append('user_id', localStorage.getItem('userId'))
      postForm(`http://43.143.179.158:8080/getStarGoods`, fd).then(res => {
        console.log(res)
        this.tableData = res.goods
      })
      .catch(function (error) {
        console.log(error);
      });
    },
    methods:{
      goodsStatus(repo)
      {
        if(repo==-1)
          return "danger";
        else 
          return "";
      },
      goDesc(row, column, event)
      {
        this.$router.push({
          path:'/goodsDesc',
          query:{
            goods:row
          }
        });
      },
    }
  }
</script>

<style scoped>
  .title{
    margin-top: 50px;
  }
  .title h3{
    /*float: left;*/
    font-size: 23px;
    color: #c91623;
  }
</style>

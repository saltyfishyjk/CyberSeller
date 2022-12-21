<template>
    <div class="dashboard">
      <div class="flex-container column">
        <div style="display: flex">
            <div class="item one" @click="clickChart('1')">
              <v-chart class="chart" :option="sellers_tmp" :update-options="true" />
            </div>
            <div class="item two" @click="clickChart('2')">
              <v-chart class="chart" :option="sellers_tmp" :update-options="true" />
            </div>
        </div>
        <div style="display: flex">
          <div class="item three" @click="clickChart('3')">
            <v-chart class="chart" :option="sellers_tmp" :update-options="true" />
          </div>
          <div class="item four active" @click="clickChart('4')">
            <v-chart class="chart" :option="sellers_tmp" :update-options="true" />
          </div>
        </div>
      </div>
    </div>

  
</template>

<script>
import { use } from 'echarts/core';
import { CanvasRenderer } from 'echarts/renderers';
import { PieChart } from 'echarts/charts';
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent,
} from 'echarts/components';
import VChart, { THEME_KEY } from 'vue-echarts';
import { postForm } from "@/api";


use([
  CanvasRenderer,
  PieChart,
  TitleComponent,
  TooltipComponent,
  LegendComponent,
]);

export default ({
  name: 'HelloWorld',
  components: {
    VChart,
  },
  provide: {
    [THEME_KEY]: 'dark',
  },
  data() {
    let sellers = this.getSellerData()
    return {
      in_seller_data: true,
      goodsList: null,
      sellers_tmp: sellers,

    };
  },
  methods: {
    getSellerData() {
      console.log('init')
      let fd = new FormData()
      var seller_name_list = []
      var seller_name2value = []
      fd.append('user_id', localStorage.getItem('userId'))
      console.log('user_id' + localStorage.getItem('userId'))
      postForm(`http://43.143.179.158:8080/analyseShopCart`, fd).then(res => {
        console.log(res)
        var data_list = res.tuples
        for (var item in data_list) {
          var row=data_list[item]
          console.log(row)
          var json_e = { value: row.price, name: row.seller_name }
          seller_name2value.push(json_e)
          seller_name_list.push(row.seller_name)
        }
      })
        .catch(function (error) {
          console.log(error);
        });
      var para_seller = {
        title: {
          text: '我的购物车',
            top: '5%',
          left: 'center',
        },
        tooltip: {
          trigger: 'item',
          formatter: '{a} <br/>{b} : {c} ({d}%)',
        },
        legend: {
          orient: 'vertical',
          left: 'left',
          data: seller_name_list
        },
        series: [
          {
            name: '卖家分布',
            type: 'pie',
            radius: '55%',
            center: ['50%', '60%'],
            data: seller_name2value,
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)',
              },
            },
          },
        ],
      }
      return para_seller
    }
  },
});
</script>

<style scoped>
.chart {
  height: 45vh;
  width: 100vh;
  margin-right: 0;
}
</style>

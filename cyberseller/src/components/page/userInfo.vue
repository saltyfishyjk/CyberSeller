<template>
    <div class="dashboard">
      <div class="flex-container column">
        <div style="display: flex">
            <div class="item one" @click="clickChart('1')">
              <div class="chart" id="mychart" ></div>
            </div>
            <div class="item two" @click="clickChart('2')">
              <v-chart class="chart" :option="sellers_tmp" :update-options="true"/>
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
import * as echarts from "echarts";

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
    let date_price = this.getDatePriceData()

    return {
      in_seller_data: true,
      goodsList: null,
      sellers_tmp: sellers,
      date_price_tmp: date_price,
      myChart: {},
      sortData: [], //动态排序数据
      myChartStyle: { float: "left", width:"100vh" , height: "400px" }, //图表样式
      dynamicSortZZTOption: {
        xAxis: {
          max: "dataMax"
        },
        yAxis: {
          type: "category",
          data: ["A", "B", "C", "D", "E","F","G"],
          inverse: true,
          animationDuration: 300,
          animationDurationUpdate: 300,
          max: 6 // only the largest 3 bars will be displayed
        },
        series: [
          {
            realtimeSort: true,
            name: "动态变化",
            type: "bar",
            data: [],
            label: {
              show: true,
              position: "right",
              valueAnimation: true
            }
          }
        ],
        legend: {
          show: true
        },
        animationDuration: 3000,
        animationDurationUpdate: 3000,
        animationEasing: "linear",
        animationEasingUpdate: "linear"
      }
    };
  },
  mounted() {
    this.myChart = echarts.init(document.getElementById("mychart"));
    // 数据初始化
    for (let i = 0; i < 7; ++i) {
      this.sortData.push(Math.round(Math.random() * 200));
    }
    // 数据刷新
    this.pageUpdate();
    setInterval(() => {
      this.pageUpdate();
    }, 3000);
  },
  methods: {
    pageUpdate() {
      console.log(this.dynamicSortZZTOption.series[0].data);
      this.dynamicSortZZTOption.series[0].data = this.sortData;
      for (let i = 0; i < this.sortData.length; ++i) {
        if (Math.random() > 0.9) {
          this.sortData[i] += Math.round(Math.random() * 2000);
        } else {
          this.sortData[i] += Math.round(Math.random() * 200);
        }
      }
      this.myChart.setOption(this.dynamicSortZZTOption);
      //随着屏幕大小调节图表
      window.addEventListener("resize", () => {
        this.myChart.resize();
      });
    },
    getDatePriceData() {

      return null
    },
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
  margin: 10px;
}
</style>

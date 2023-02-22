<template>
    <div id="myEchart" ref="myEchart" style="width: 600px;height:600px"></div>
    <el-select v-model="select_value" @change="changeData($event)" placeholder="Select" size="large">
        <el-option label="sine" value='sine' />
        <el-option label="step" value='step' />
    </el-select>
</template>

<script setup lang='ts'>
// vue
import { onMounted, ref } from 'vue'

// echarts
import * as echarts from 'echarts'

// store
import { useStore } from '../store';
import { storeToRefs } from 'pinia';

// utilies
import { get_max, get_min } from '../../utilies/utilies'

const store = useStore()
const { self_Adapting } = storeToRefs(store)

// data series
let dataseries = [{
    name: 'new_actual_position',
    type: 'line',
    smooth: true,
    data: [],
    symbolSize: 0.1,
    symbol: 'circle',
    label: { show: false, fontSize: 16 },
    labelLayout: { dx: -20 },
    encode: { label: 2, tooltip: 1 },
    color: 'blue',
},
{
    name: 'Command_Position',
    type: 'line',
    smooth: true,
    data: [],
    symbolSize: 0.1,
    symbol: 'rect',
    label: { show: false, fontSize: 16 },
    labelLayout: { dx: -20 },
    encode: { label: 2, tooltip: 1 },
    color: 'red',
},
{
    name: 'Following-Error',
    type: 'line',
    smooth: true,
    data: [],
    symbolSize: 0.1,
    symbol: 'triangle',
    label: { show: false, fontSize: 16 },
    labelLayout: { dx: -20 },
    encode: { label: 2, tooltip: 1 },
    color: 'orange',
    yAxisIndex: 1,
},
{
    name: 'new_following_error',
    type: 'line',
    smooth: true,
    data: [],
    symbolSize: 0.1,
    symbol: 'triangle',
    label: { show: false, fontSize: 16 },
    labelLayout: { dx: -20 },
    encode: { label: 2, tooltip: 1 },
    color: 'green',
    yAxisIndex: 1,
}]



let select_value = ref('');

let option = {
    animationDuration: 10000,
    title: {
        text: "Self-Adapting Experiment",
        subtext: 'sine.txt',
        left: 'center',
    },
    tooltip: {
        trigger: "axis",
        axisPointer: {
            type: 'cross'
        }
    },
    xAxis: {
        splitLine: {
            lineStyle: {
                type: 'dashed'
            }
        }
    },
    yAxis: [
        {
            splitLine: {
                lineStyle: {
                    type: 'dashed'
                },
            },
            min: get_min,
            max: get_max,
        },
        {
            splitLine: {
                lineStyle: {
                    type: 'dashed'
                },
            },
            min: get_min,
            max: get_max,
        }
    ],
    legend: {
        bottom: 5
    },

    series: [

    ],

}

var myChart: echarts.ECharts;

onMounted(() => {
    // 基于准备好的dom，初始化echarts实例
    myChart = echarts.init(document.getElementById('myEchart') as HTMLElement);
    // 绘制图表
    myChart.setOption(option);
})

// change data source according to the value of the selector
const changeData = (e: string) => {
    // To let the echarts draw the data again.
    myChart.clear()

    dataseries.forEach((element: any) => {
        element.data = self_Adapting.value['result'][e][element.name]
    });
    option.title.subtext = e + '.txt';
    option.series = dataseries;

    myChart.setOption(option)
}


</script>

<style></style>
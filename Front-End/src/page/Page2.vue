<template>
  <div>
    Power Cost (per min): <span :style="power_cos">{{ form[0].value * 60 }}</span> J<br>
    Welding Speed (per min): <span :style="weld_spd">{{ form[1].value }}</span> m<br>
    Material consumption (per min): <span :style="gas_fr">{{ form[2].value }}</span> L<br>
  </div>
  <div class="main_container">
    <div class="left_container">
      <!-- @TODO: let _id to be auto asigned -->
      <!-- _id: indicates the component that which industrial process to be shown. -->
      <!-- focus-change: get the id of the focued input element of the component -->
      <Params :_id="0" @focus-change="get_focus" @input-change="setFontColor"></Params>
    </div>
    <div class="right_container">
      <div class="img-container">
        <!-- The img would change based of which input element is being focused -->
        <ElImage :src="focus_img" fit="scale-down"></ElImage>
      </div>
    </div>
  </div>
</template>

<script setup lang='ts'>
// vue
import { ref } from 'vue'

// store
import { storeToRefs } from 'pinia';
import { useStore } from '../components/store';

// components
import Params from '../components/Form/params.vue'

// utilies
import { getColorByBaiFenBi } from '../utilies/utilies';

// types
import { n2s, input_change_type, } from '../types/types'

const store = useStore()
const { processes_list } = storeToRefs(store)

let form = processes_list.value[0].params


// the id of focused input element in the Params component
let focus_id = ref(0)
// In el-image component
let focus_img = ref('src/assets/img/2base.png')

//
const focus_id_2_img: n2s = {
  0: 'src/assets/img/2base.png',
  1: 'src/assets/img/2base.png',
  2: 'src/assets/img/welding_speed.png',
  3: 'src/assets/img/gas_flow_rate.png',
  4: 'src/assets/img/focal_position.png',
  5: 'src/assets/img/angular_position.png',
  6: 'src/assets/img/material_thickness.png'
}

// get focused_id from Params component and then change the img
const get_focus = (id: number) => {
  focus_id.value = id
  console.log('get_focus', focus_id.value);
  focus_img.value = focus_id_2_img[id]
}

const setFontColor = (item: input_change_type) => {
  console.log(item);

  if (item.name == "power (W)") {
    power_cos.color = getColorByBaiFenBi((item.value - form[0].min) / (form[0].max - form[0].min) * 100)
  }
  else if (item.name == "welding speed (m/min)") {
    weld_spd.color = getColorByBaiFenBi((form[1].max - item.value) / (form[1].max - form[1].min) * 100)
  }
  else {
    gas_fr.color = getColorByBaiFenBi((item.value - form[2].min) / (form[2].max - form[2].min) * 100)
  }
}

// style for fonts
let power_cos = {
  "color": 'green',
  "font-size": "20px"
}

let weld_spd = {
  "color": 'green',
  "font-size": "20px"
}

let gas_fr = {
  "color": 'green',
  "font-size": "20px"
}

</script>

<style lang="less" scoped>
.main_container {
  display: inline-flex;
  width: 80%;
  height: 80%;
}

.left_container {
  width: 40%;
  max-height: 600px;
  overflow: auto;
  display: grid;
  place-items: center;
}

.right_container {
  width: 70%;
  max-height: 700px;
  overflow: hidden;
  display: grid;
  place-items: center;
}

.img {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
}

.img-container {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
</style>
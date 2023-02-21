<template>
  <div class="main_container">
    <div class="left_container">
      <Upload v-if="!Flags.Upload" @on-submit="submit"></Upload>
      <Parameters v-if="Flags.Upload"></Parameters>
    </div>


    <div class="right_container">
      <ElButton v-if="!Flags.Processes" @click="getProcesses">Get Processes</ElButton>
      <Process v-if="Flags.Processes" v-for="(item, index) in processes_list" :_id="index"></Process>
    </div>
  </div>
</template>

<script setup lang='ts'>

// axios
import axios from 'axios'

// pinia
import { useStore } from '../components/store'
import { storeToRefs } from 'pinia'

// components
import Upload from '../components/Upload/index.vue'
import Parameters from '../components/Draggable/Parameters.vue'
import Process from '../components/Draggable/Process.vue'

// api
import { getProcesses } from '../api/api'

// variables
const store = useStore();
let { processes_list, Flags } = storeToRefs(store)

// funcs
const submit = (re: boolean) => {
  Flags.value.Upload = re;
  console.log('isUploaded', Flags.value.Upload);
}


</script>

<style scoped lang='less'>
.main_container {
  display: inline-flex;
  width: 80%;
  height: 80%;
}

.left_container {
  width: 50%;
  max-height: 600px;
  overflow: auto;
}

.right_container {
  width: 50%;
  max-height: 600px;
  overflow: auto;
  display: grid;
  place-items: center;
}
</style>
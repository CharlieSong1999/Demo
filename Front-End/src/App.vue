<template>

  <!-- ============================================================== -->
  <el-header style="height: 150px">
    <div class="content content-header">
      <Header :activeNum="activeNum"></Header>
    </div>
  </el-header>
  <!-- ============================================================== -->

  <!-- ============================================================== -->
  <el-main style="min-height: 600px;">
    <router-view></router-view>
  </el-main>
  <!-- ============================================================== -->

  <!-- ============================================================== -->
  <!-- Two buttons to step forward or backward -->
  <el-footer style="height: 50px">
    <div class="content content-footer">
      <el-button @click="changeStep(-1)" type="primary" :icon="ArrowLeft">
        Previous Page
      </el-button>
      <el-button type="primary" @click="changeStep(1)">
        Next Page
        <el-icon class="el-icon--right">
          <ArrowRight />
        </el-icon>
      </el-button>
    </div>
  </el-footer>
  <!-- ============================================================== -->

</template>

<script lang="ts" setup>
/*
 * Imports
 */
import Header from './components/Header/index.vue'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useStore } from './components/store';
import { storeToRefs } from 'pinia';
import { ElMessage, ElMessageBox } from 'element-plus';
import {
  ArrowLeft,
  ArrowRight,
} from '@element-plus/icons-vue'
import axios from 'axios';
import { cloneDeep } from 'lodash';

/*
 * Variables
 */
const store = useStore()
const { Flags, recommend_param, Status, self_Adapting } = storeToRefs(store)
const router = useRouter()

let activeNum = ref<number>(0)

/*
 * Functions
 */
const checkStep1 = () => {
  if (!Flags.value.Upload || !Flags.value.Processes) {
    ElMessage({
      showClose: true,
      message: 'Please upload your data file and allocate them to appropriate industrial process to go to the next page!',
      type: 'warning',
    })
    return false;
  }
  return true;
}

/*
 * receive recommended parameter list from back-end server.
 */
const get_recommend = () => {
  const api = '/api/getRecommend'
  axios.get(api).then((res: any) => {
    const data = res.data;
    console.log('get Recommend reply: ', data);

    recommend_param.value = cloneDeep(data);
    console.log('recommend_param.value', recommend_param.value);
    Status.value.Btn_recommend_loading = false
    Flags.value.Recommend = true
  })
}

/*
 * receive self adapting result from back-end server
 */
const getSelfAdapting = () => {
  const api = '/api/selfAdapting'
  axios.get(api).then((res: any) => {
    const data = res.data;
    console.log('self-adapting reply: ', data);

    self_Adapting.value['result'] = cloneDeep(data);
    console.log('self_Adapting.value', self_Adapting.value);
  })
}


const Step = (num: number) => {
  // step forward
  if (num > 0 && (activeNum.value + 1) <= Status.value.Page) {
    activeNum.value++;
  } // step backward
  else if (num < 0 && (activeNum.value - 1) >= 0) {
    activeNum.value--;
  }

  router.push('Page' + activeNum.value);
}



const changeStep = (num: any) => {

  if (activeNum.value == 0 && num > 0) {
    // check if statisfy the requirement of the first step.
    if (checkStep1()) {
      if (Status.value.Page < 1) {

        Status.value.Page = 1;

        ElMessageBox.confirm(
          'Upload all Data?',
          'Warning',
          {
            confirmButtonText: 'OK',
            cancelButtonText: 'Cancel',
            type: 'warning',
          }
        )
          .then(() => {
            ElMessage({
              type: 'success',
              message: 'Data uploaded',
            })
            Step(num);
            get_recommend();
          })
          .catch(() => {
            ElMessage({
              type: 'info',
              message: 'Upload canceled',
            })
          })
      }
      else {
        ElMessageBox.confirm(
          'Re-upload all Data?',
          'Warning',
          {
            confirmButtonText: 'OK',
            cancelButtonText: 'Keep old data',
            type: 'warning',
          }
        )
          .then(() => {
            ElMessage({
              type: 'success',
              message: 'Data uploaded',
            })
            Step(num);
            get_recommend();
          })
          .catch(() => {
            ElMessage({
              type: 'info',
              message: 'Keep old data',
            })
            Step(num);
          })
      }
    }
  }
  else if (activeNum.value == 1 && num > 0) {
    if (Status.value.Page < 2) {
      Status.value.Page = 2;
      console.log('Status.value.Page', Status.value.Page);

    }
    getSelfAdapting();
    Step(num)
  }
  else {
    Step(num);
  }


}

</script>

<style scoped lang='less'>
.content {
  text-align: center;
  background-color: #fff;
  border-radius: 20px;
  position: relative;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}

.content-main {
  margin: 0 auto;
  text-align: center;
  height: 100%;
  max-width: 70%;
  top: 50%;
  transform: translate(0, 50%);
}

.el-main {
  display: grid;
  place-items: center;
}


html,
body,
#app {
  height: 100%;
  width: 100%;
  overflow: hidden;
}
</style>

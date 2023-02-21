<template>
  <div class="container">
    <el-upload ref="upload" action="/api/upload" method='post' :on-change="fileChange" :auto-upload="false"
      accept=".rar,.zip,.gz,.gz.tar,.tar" :on-exceed="handleExceed" :limit="1" drag :file-list="fileList"
      :on-success="upload_success" style="width: 70%; heigth: 50%">

      <el-icon class="el-icon--upload"><upload-filled /></el-icon>

      <div class="el-upload__text">
        Drop file here or <em>click to upload</em>
      </div>

      <template #tip>
        <div class="el-upload__tip">
          <font style="font-color: red;">limit 1 file, new file will cover the old file</font> <br>
          rar, zip, gz, tar, gz.tar files only.
        </div>

      </template>

    </el-upload>

    <el-button class="ml-3 el-button-center" type="success" @click="submitUpload">
      upload to server
    </el-button>
  </div>
</template>


<script lang="ts" setup>
import { ref } from 'vue'
import { UploadFilled } from '@element-plus/icons-vue'

// element ui upload component
import { genFileId } from 'element-plus'
import type { UploadInstance, UploadProps, UploadRawFile, UploadFile, UploadFiles } from 'element-plus'
// element ui message component
import { ElMessage } from 'element-plus'

// pinia
import { useStore } from '../store'

const store = useStore()

// emit message to father component
const emit = defineEmits([
  'on-submit'
])


// element ui upload component
// reference to the upload div aka the upload instance
const upload = ref<UploadInstance>()
const fileList: UploadRawFile[] = []

// handle the event when the file number exceed 1
const handleExceed: UploadProps['onExceed'] = (files) => {
  upload.value!.clearFiles()
  const file = files[0] as UploadRawFile
  file.uid = genFileId()
  upload.value!.handleStart(file)
  console.log(fileList);

}

// handle the event when the file change
const fileChange = (file: UploadFile, fileList: UploadFiles) => {

  const fileSuffix = file.name.substring(file.name.lastIndexOf(".") + 1);
  const whiteList = ["rar", "zip", "gz", "tar", "gz.tar"];

  if (whiteList.indexOf(fileSuffix) === -1) {
    ElMessage({
      showClose: true,
      message: 'Only rar, zip, gz, tar, gz.tar files are accepted.',
      type: 'error',
    })
    upload.value!.clearFiles()
    return false;
  }

}

// upload the file
const submitUpload = () => {
  upload.value!.submit()
}

// receive response
const upload_success = (res: any, file: any, fileListL: any) => {
  store.setDataList(res);
  emit('on-submit', true);
}


</script>

<style scoped lang='less'>
.el-button-center {
  position: relative;

  span {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
}

.container {
  display: grid;
  place-items: center;
  width: 80%;
  height: 80%;
}
</style>
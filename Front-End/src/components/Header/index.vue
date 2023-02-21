<template>
  <el-steps :active="activeNum" align-center>
    <el-step title="Data Input" :icon="UploadFilled" />
    <el-step title="Control Parameters Recommendation" :icon="Histogram" />
    <el-step title="Control Parameters Self-Adapting" :icon="DataBoard" />
  </el-steps>
</template>

<script setup lang="ts">
import { DataBoard, Histogram, UploadFilled } from '@element-plus/icons-vue'

const props = defineProps<{
  activeNum: number
}>()
</script>

<style>

</style>
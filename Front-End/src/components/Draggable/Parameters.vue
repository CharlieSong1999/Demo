<template>
    <div>
        <el-card class="Parameters">
            <template #header>
                <div class="card-header">
                    <span>Data Sets</span>
                </div>
            </template>

            <draggable :list="data_list" :group="{ name: 'Page2', pull: 'clone', put: false }" ghost-class="ghost"
                item-key="id">
                <template #item="{ element }">
                    <el-space warp>
                        <el-card shadow="always"> {{ element }} </el-card>
                    </el-space>
                </template>
            </draggable>

        </el-card>
    </div>
</template>

<script setup lang='ts'>
import draggable from 'vuedraggable'
import { storeToRefs } from 'pinia'
import { useStore } from '../store'

const store = useStore()
const { data_list, } = storeToRefs(store);
</script>

<style lang="less" scoped>

</style>
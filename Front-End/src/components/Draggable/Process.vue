<template>
    <div style="display: block; min-width: 300px;">
        <el-card class="cards-first">
            <template #header>
                <div class="card-header">
                    <span style="margin: 10% 10% 10% 10%">{{ name }}</span>
                </div>
            </template>
            <draggable :list="list" group="Page2" item-key="id">
                <template #item="{ element }">
                    <el-space>
                        <el-tag class="mx-1" closable size="large" @close="tagClose(list, element)">
                            {{ element }}
                        </el-tag>
                    </el-space>

                </template>

            </draggable>
        </el-card>
    </div>
</template>

<script setup lang='ts'>

// draggable
import draggable from 'vuedraggable'

// pinia
import { useStore } from '../store'
import { storeToRefs } from 'pinia'

const store = useStore()

const { processes_list, } = storeToRefs(store)

const props = defineProps<{
    _id: number,
}>()

const _id = props._id;

const list = processes_list.value[_id].param_file;
const name = processes_list.value[_id].name;

const tagClose = (list: any, element: any) => {
    list.splice(list.indexOf(element), 1)
}

</script>

<style lang='less' scoped>
.process-cards {
    text-align: center;
    background-color: #fff;
    border-radius: 20px;
}

.parameter-card {
    text-align: center;
    background-color: #fff;
    border-radius: 20px;
    max-width: 600px;
    position: relative;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
}

.cards-first {
    margin: 0px 0px 20px 0px;
}

.cards-last {
    margin: 20px 0px 0px 0px;
}
</style>
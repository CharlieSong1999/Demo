<template>
    <el-form :model="form" label-width="200px">
        <el-form-item v-for="item in form" :label="item.name" styel="font-size:large;">
            <el-input-number @focus="input_focus(item.name)" @blur="input_blur" @change="emit_input_value(item)"
                v-model="item.value" :min="item.min" :max="item.max" :step="item.step" />
            <div class="range"> range:[ {{ item.min }}, {{ item.max }} ]</div>
        </el-form-item>
    </el-form>
    <ElButton :loading="Status.Btn_recommend_loading" type="primary" @click="setValue">Recommend</ElButton>
</template>

<script setup lang='ts'>
import { ref } from 'vue'
import { storeToRefs } from 'pinia';
import { useStore } from '../store';

const store = useStore()
const { processes_list, recommend_param, Status, Flags } = storeToRefs(store)

const props = defineProps<{
    _id: number,
}>()
const emit = defineEmits(['focus-change', 'input-change'])


type param_item = {
    name: string,
    value: number,
    min: number,
    max: number,
    step: number
}

let form = processes_list.value[props._id].params
let focus_id = ref(0)


// set the value of form to be the recommended value received 
// from the server.
const setValue = () => {

    // If the recommended value yet to receive, set the 'recommend'
    // Btn to loading status.
    if (!Flags.value.Recommend) {
        Status.value.Btn_recommend_loading = true;
        return;
    }

    const re_params = recommend_param.value;

    form.forEach((form_item) => {
        // console.log('form_item', form_item, 'form_item.value', form_item.value, 'form_item.name', form_item.name);
        form_item.value = re_params[form_item.name]
        emit_input_value(form_item)
    })
}

form = processes_list.value[props._id].params

const input_focus = (name: string) => {
    console.log(form);
    form.forEach((item, index) => {
        if (item.name == name) {
            focus_id.value = index + 1;
        }
    })
    emit('focus-change', focus_id.value)
    // console.log(focus_id.value);
}

const input_blur = (e: any) => {
    focus_id.value = 0;
    // emit('focus-change', focus_id.value)
    // console.log(focus_id.value);
}
// console.log('_id', props._id, 'processes_list.value[props._id].params', processes_list.value[props._id].params);
// console.log('form.value', form.value);

// emit input value
const emit_input_value = (item: param_item) => {
    if (item.name == 'power (W)' || item.name == "welding speed (m/min)" || item.name == "gas flow rate (l/min)") {
        emit('input-change', { "name": item.name, "value": item.value })
    }
}

</script>

<style lang='less' scoped>
.range {
    font-size: smaller;
    color: grey;
}
</style>
import { Status } from "./../../types/types";
import { defineStore } from "pinia";
import { Names } from "./store-names";

// types

// Stand for recommended parameters
// index: string,  the name of the parameter
// value: number, the value of the parameter

export const useStore = defineStore(Names.STORE, {
  state: (): State => {
    return {
      data_list: [],
      processes_list: [],
      recommend_param: {},
      Flags: {
        Processes: false,
        Upload: false,
        Recommend: false,
        selfAdapting: false,
      },
      Status: {
        Btn_recommend_loading: false,
        Page: 0,
      },
      self_Adapting: { result: {} },
    };
  },
  // computed 修饰一些值
  getters: {},
  // methods 同步异步 提交state
  actions: {
    setDataList(data_list: []) {
      this.data_list = data_list;
    },
    setProcessesList(list: []) {
      let tmp_list: any = [];
      list.forEach((item: any) => {
        tmp_list.push({
          name: item.name,
          params: item.params,
          param_file: [],
        });
      });
      this.processes_list = tmp_list;
    },
  },
});

export type { selfAdaptingResult };

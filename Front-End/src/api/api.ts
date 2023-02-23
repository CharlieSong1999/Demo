import { selfAdapting } from "./../types/types";
import { useStore } from "./../components/store/index";
import { storeToRefs } from "pinia";
// axios
import axios from "axios";

// deepclone
import { cloneDeep } from "lodash";

// store

export const getProcesses = () => {
  const api = "/api/getprocesses";

  const store = useStore();

  const { Flags } = storeToRefs(store);

  axios.get(api).then((res) => {
    console.log("receive processes data", res.data);
    store.setProcessesList(res.data);
    Flags.value.Processes = true;
  });
};

/*
 * receive recommended parameter list from back-end server.
 */
export const get_recommend = () => {
  const api = "/api/getRecommend";

  const store = useStore();

  const { Flags, Status, processes_list, recommend_param } = storeToRefs(store);

  let paths = [];
  processes_list.value.forEach((p) => {
    if (p.name == "Laser Welding") {
      paths = p.param_file;
    }
  });

  axios
    .get(api, {
      params: {
        paths: paths,
      },
    })
    .then((res: any) => {
      const data = res.data;
      console.log("get Recommend reply: ", data);

      recommend_param.value = cloneDeep(data);
      console.log("recommend_param.value", recommend_param.value);
      Status.value.Btn_recommend_loading = false;
      Flags.value.Recommend = true;
    });
};

/*
 * receive self adapting result from back-end server
 */
export const getSelfAdapting = () => {
  const api = "/api/selfAdapting";

  const store = useStore();

  const { self_Adapting, processes_list } = storeToRefs(store);

  let paths = [];
  processes_list.value.forEach((p) => {
    if (p.name == "Self Adapting") {
      paths = p.param_file;
    }
  });

  axios
    .get(api, {
      params: {
        paths: paths,
      },
    })
    .then((res: any) => {
      const data = res.data;
      console.log("self-adapting reply: ", data);

      self_Adapting.value["result"] = cloneDeep(data);
      console.log("self_Adapting.value", self_Adapting.value);
    });
};

import { useStore } from "./../components/store/index";
// axios
import axios from "axios";

// store
const store = useStore();
import { storeToRefs } from "pinia";
const { Flags } = storeToRefs(store);

export const getProcesses = () => {
  const api = "/api/getprocesses";

  axios.get(api).then((res) => {
    console.log("receive processes data", res.data);
    store.setProcessesList(res.data);
    Flags.value.Processes = true;
  });
};

import {
  createRouter,
  createWebHistory,
  createWebHashHistory,
  createMemoryHistory,
  RouteRecordRaw,
} from "vue-router";
import { useStore } from "../components/store/index";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    redirect: "/Page0",
  },
  {
    path: "/Page0",
    component: () => import("../page/Page1.vue"),
    meta: {
      keepAlive: true,
      showFooter: true,
    },
  },
  {
    path: "/Page1",
    component: () => import("../page/Page2.vue"),
    meta: {
      keepAlive: true,
      showFooter: true,
    },
    beforeEnter: (to, from) => {
      const Status = useStore().Status;
      console.log(Status);

      if (Status.Page < 1) {
        return "/Page0";
      } else {
        return true;
      }
    },
  },
  {
    path: "/Page2",
    component: () => import("../page/Page3.vue"),
    meta: {
      keepAlive: true,
      showFooter: true,
    },
    beforeEnter: (to, from) => {
      const Status = useStore().Status;
      if (Status.Page < 2) {
        if (Status.Page == 1) {
          return "/Page1";
        } else {
          return "/Page0";
        }
      } else {
        return true;
      }
    },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;

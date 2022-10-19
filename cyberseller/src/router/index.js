import { createRouter, createWebHistory } from "vue-router"

const HelloWorld = () => import("../components/HelloWorld")
const myLayout = () => import("../components/myLayout")

const routes = [
    { path: '/', redirect: '/home' },
    { path: '/helloworld', name: 'helloworld', component: HelloWorld },
    { path: '/mylayout', name: 'layout', component: myLayout }
]
const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router

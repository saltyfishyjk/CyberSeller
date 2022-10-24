import { createRouter, createWebHistory } from "vue-router"

const HelloWorld = () => import("../components/HelloWorld")
const myLayout = () => import("../components/myLayout")

const routes = [
    { path: '/', redirect: '/home' },
    { path: '/home', name: 'layout', component: myLayout },
    { path: '/helloworld', name: 'helloworld', component: HelloWorld }
]
const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router

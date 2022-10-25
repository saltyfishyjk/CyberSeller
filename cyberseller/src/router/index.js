import { createRouter, createWebHistory } from "vue-router"

const HelloWorld = () => import("../components/HelloWorld")
const myLayout = () => import("../components/myLayout")
const LoginPage = () => import("../components/LoginPage")

const routes = [
    { path: '/', redirect: '/market' },
    {
        path: '/market',
        name: 'layout',
        component: myLayout,
    },
    {
        path: '/shopCart',
        name: 'shopCart',
        component: HelloWorld
    },
    {
        path: '/login',
        name: 'login',
        component: LoginPage
    }
]
const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router

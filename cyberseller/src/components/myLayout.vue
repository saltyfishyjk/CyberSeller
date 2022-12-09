<template>
    <div class="myLayout">
        <LayoutHeader></LayoutHeader>
        <LayoutNavbar></LayoutNavbar>
        <LayoutMain></LayoutMain>
        <CartList></CartList>
        <RouterView></RouterView>
    </div>
</template>

<script>
import LayoutMain from './LayoutComponents/LayoutMain';
import LayoutHeader from './LayoutComponents/LayoutHeader';
import LayoutNavbar from './LayoutComponents/LayoutNavbar';
export default {
    name:"myLayout",
    data() {
        return {};
    },

    components: {
    LayoutHeader,
    LayoutMain,
    LayoutNavbar,
    CartList
},

    methods: {}
};
</script>

<style >
.LayoutHeader {
    position: absolute;
    line-height: 50px;
    background-color: #2d333b;
    top: 0px;
    left: 0px;
    right: 0px;
}

.LayoutNavbar {
    /* position: absolute; 
     background-color: #adbac7; 
    top: 50px;
    left: 0px;
    bottom: 0px;*/
    width: 180px;  
    height:100%;
    overflow-y: auto;
} 

.LayoutMain {
    position: absolute;
    left: 200px;
    /* 内部框框距离 */
    top: 50px;
    padding: 10px;
    right: 0px;
    overflow-y: auto;
    bottom: 0px;
    /* background-color: rebeccapurple; */
}
</style>

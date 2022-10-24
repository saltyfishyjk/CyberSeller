<template #title>
    <div class="LayoutNavbar">
        <el-menu default-active="1-4-1" class="el-menu-vertical-demo" @mouseover="mouseOver" @mouseleave="mouseLeave" 
            :collapse="isCollapse">
            <el-menu-item index="1">
                <i class="el-icon-menu"></i>
                <img class="icon_format" src="../../assets/market.png">
                <template #title>
                    Market
                </template>
            </el-menu-item>
            <el-menu-item index="2">
                <i class="el-icon-menu"></i>
                <img class="icon_format" src="../../assets/shopCart.png">
                <template #title>
                    Shop Cart
                </template>
            </el-menu-item>
            <el-menu-item index="3">
                <i class="el-icon-menu"></i>
                <img class="icon_format" src="../../assets/history.png">
                <template #title>
                    History
                </template>
            </el-menu-item>
            <el-menu-item index="4">
                <i class="el-icon-menu"></i>
                <img class="icon_format" src="../../assets/settings.png">
                <template #title>
                    Settings
                </template>
            </el-menu-item>
        </el-menu>
    </div>
</template>

<script>
export default {
    data() {
        return {
            isCollapse: true,
        }
    },
    methods: {
        mouseOver: function () {
            this.isCollapse = false;
        },
        mouseLeave: function () {
            this.isCollapse = true;
        },
    },
}
</script>
<style>
.el-menu-vertical-demo:not(.el-menu--collapse) {
    width: 170px;
    height: 100%;
    background-color: white;
    border-style: none inset inset none;
}


.el-menu-vertical-demo {
    height: 100%;
    background-color: white;
    border-style:none inset inset none;
}

.icon_format {
    height: 2em;
    margin-right: 5px;
}
</style>

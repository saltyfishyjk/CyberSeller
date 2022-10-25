<template>
    <div class="LayoutHeader">
        <a href>
            <img class="logo" src="../../assets/logo.png" alt width="30px" />
            <span class="company">CyberSeller</span>
        </a>
        <el-dropdown class="el-dropdown">
            <span class="el-dropdown-link">
                Account<i class="el-icon-arrow-down el-icon--right"></i>
            </span>
            <template #dropdown>
                <el-dropdown-menu>
                    <el-dropdown-item>Login</el-dropdown-item>
                    <el-dropdown-item>Sign Up</el-dropdown-item>
                    <!-- <el-dropdown-item disabled>tag1</el-dropdown-item>
                    <el-dropdown-item divided>tag2</el-dropdown-item> -->
                </el-dropdown-menu>
            </template>
        </el-dropdown>
    </div>
</template>

<script>
export default {
    data() {
        return {};
    },
    components: {},

    methods: {
        handleCommand(command) {
            alert(command)
        }
    }
};
</script>


<style scoped>
.logo {
    vertical-align: middle;
    padding: 0px 10px 0 40px;
}

.company {
    position: absolute;
    color: aliceblue;
}

.el-dropdown {
    float: right;
    /* color: aliceblue; */
    margin:20px;
}

.el-dropdown-link {
    color: white;
    /* 定义放上去手的形状 */
    cursor: pointer;
}
</style>

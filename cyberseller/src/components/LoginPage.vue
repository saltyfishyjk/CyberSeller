<template>
    <LayoutHeader></LayoutHeader>
    <LayoutNavbar></LayoutNavbar>
    <div class="login">
        <el-tabs type="border-card">
            <el-tab-pane label="登录">
                <el-form label-position="right" label-width="60px" style="max-width: 460px" class="loginForm">
                    <el-form-item label="邮箱：">
                        <el-input v-model="LoginInfo.tryLoginForm.tryLoginEmail" />
                    </el-form-item>
                    <el-form-item label="密码：">
                        <el-input type="password" v-model="LoginInfo.tryLoginForm.tryLoginPassword" />
                    </el-form-item>

                    <el-row>
                        <el-checkbox class="checkBox" v-model="LoginInfo.tryLoginForm.tryLoginIsAgree" label="同意用户使用准则" name="type" />
                    </el-row>
                    <el-button v-if="LoginInfo.tryLoginForm.tryLoginIsAgree" type="primary" class="loginBtn" @click="login">
                        登录
                    </el-button>
                </el-form>
            </el-tab-pane>

            <el-tab-pane label="注册">
                <el-form label-position="right" label-width="100px" style="max-width: 460px" class="loginForm">
                    <el-form-item label="邮箱：">
                        <el-input v-model="LoginInfo.tryRegisterForm.tryRegisterEmail" />
                    </el-form-item>
                    <el-form-item label="密码：">
                        <el-input type="password" v-model="LoginInfo.tryRegisterForm.tryRegisterPassword" />
                    </el-form-item>
                    <el-form-item label="确认密码：">
                        <el-input type="password" v-model="LoginInfo.tryRegisterForm.tryRegisterConfirmedPassword" @blur="confirmFunc" />
                    </el-form-item>
                    <el-form-item label="验证码：">
                        <el-row>
                            <el-input type="password" v-model="LoginInfo.tryRegisterForm.tryRegisterIdentifyCode" class="inpWidth" />
                            <el-button type="primary" @click="getIdentifyCode" plain>
                                获取验证码
                            </el-button>
                        </el-row>
                    </el-form-item>

                    <el-row>
                        <el-checkbox class="checkBox" v-model="LoginInfo.tryRegisterForm.tryRegisterIsAgree" label="同意用户使用准则" name="type" />
                    </el-row>
                    <el-button v-if="LoginInfo.tryRegisterForm.tryRegisterIsAgree" type="primary" class="loginBtn" @click="register">
                        注册
                    </el-button>
                </el-form>
            </el-tab-pane>
        </el-tabs>
    </div>
</template>
<script>
import { ElMessage } from "element-plus";
import { LoginInfo } from "@/utils/LoginInfo";
import LayoutHeader from './LayoutComponents/LayoutHeader.vue';
import LayoutNavbar from './LayoutComponents/LayoutNavbar.vue';
export default {
    data() {
        return {
            LoginInfo
        }
    },
    methods: {
        login() {
            console.log(LoginInfo.tryLoginForm);
        },
        register() {
            console.log("注册", LoginInfo.tryRegisterForm);
        },
        getIdentifyCode() {
            console.log("获取验证码");
        },
        confirmFunc(){
            if (LoginInfo.tryRegisterForm.tryRegisterPassword !== LoginInfo.tryRegisterForm.tryRegisterConfirmedPassword)
                ElMessage.error("密码与确认密码不一致.");
        }
    },
    components: { LayoutHeader, LayoutNavbar }
};
</script>

<style scoped>
.login {
    position: absolute;
    left: calc(50% - 200px);
    top: 20%;
    width: 400px;
}

.loginBtn {
    width: 100px;
}

.loginForm {
    text-align: center;
}

.checkBox {
    margin-left: 7px;
}

.inpWidth {
    width: 165px;
}
</style>

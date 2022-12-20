<template>
    <div class="login-wrap">
        <div class="ms-login">
            <div class="ms-title">CyberSeller</div>
            <el-form :model="param" :rules="rules" ref="login" label-width="0px" class="ms-content">
                <el-form-item prop="username">
                    <el-input v-model="param.username" placeholder="username">
                        <el-button slot="prepend" icon="el-icon-lx-people"></el-button>
                    </el-input>
                </el-form-item>
                <el-form-item prop="password">
                    <el-input type="password" placeholder="password" v-model="param.password"
                        @keyup.enter.native="submitForm()">
                        <el-button slot="prepend" icon="el-icon-lx-lock"></el-button>
                    </el-input>
                </el-form-item>
                <el-form-item prop="confirmed">
                    <el-input type="password" placeholder="password" v-model="param.confirmed" @keyup.enter.native="submitForm()">
                        <el-button slot="prepend" icon="el-icon-lx-lock"></el-button>
                    </el-input>
                </el-form-item>
                <div class="register-btn">
                    <el-button type="primary" @click="submitForm()">注册并登录</el-button>
                </div>
            </el-form>
        </div>
    </div>
</template>

<script>
import { userSignUp } from "@/api";
export default {
    data: function () {
        return {
            param: {
                username: '',
                password: '',
                confirmed: ''
            },
            rules: {
                username: [{ required: true, message: '请输入用户名', trigger: 'blur' }],
                password: [{ required: true, message: '请输入密码', trigger: 'blur' }],
                confirmed: [{ required: true, message: '请确认密码', trigger: 'blur' }],
            },
        };
    },
    methods: {
        submitForm() {
            if (this.param.password != this.param.confirmed) { 
                this.$message.error('请确保前后密码一致!');
                return false;
            }
            userSignUp(this.param).then(res => {
                let name = localStorage.getItem('username')
                if (name != 'admin') {
                    this.$message.success('注册成功!');
                    this.$router.push('/');
                } else {
                    this.$message.error('注册失败,该用户名已被注册!');
                    console.log(res);
                    return false;
                }
            }
            )
        }
    },
};
</script>

<style scoped>
.login-wrap {
    position: relative;
    width: 100%;
    height: 100%;
    background-size: 100%;
}

.ms-title {
    width: 100%;
    line-height: 50px;
    text-align: center;
    font-size: 20px;
    color: #fff;
    border-bottom: 1px solid #ddd;
}

.ms-login {
    position: absolute;
    left: 50%;
    top: 50%;
    width: 350px;
    margin: -190px 0 0 -175px;
    border-radius: 5px;
    background: rgba(255, 255, 255, 0.3);
    overflow: hidden;
}

.ms-content {
    padding: 30px 30px;
}

.register-btn {
    text-align: center;
}

.register-btn button {
    width: 100%;
    height: 36px;
    margin-bottom: 10px;
}
</style>

// LoginInfo.js
import { reactive } from 'vue'

export const LoginInfo = reactive({
    curLoginState: false,
    curLoginId: "",
    
    tryLoginForm: {
        tryLoginName: "",
        tryLoginEmail: "",
        tryLoginPassword: "",
        tryLoginIsAgree:false
    },

    tryRegisterForm: {
        tryRegisterName: "",
        tryRegisterEmail: "",
        tryRegisterPassword: "",
        tryRegisterConfirmedPassword: "",
        tryRegisterIdentifyCode:"",
        tryRegisterIsAgree: false    
    },

    count: 0
})

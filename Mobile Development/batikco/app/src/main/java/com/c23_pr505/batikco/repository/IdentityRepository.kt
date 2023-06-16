package com.c23_pr505.batikco.repository

import com.c23_pr505.batikco.response.login.ResponseLogin
import com.c23_pr505.batikco.remote.ApiService
import com.c23_pr505.batikco.response.login.LoginRequest
import com.c23_pr505.batikco.response.register.RegisterRequest
import com.c23_pr505.batikco.response.register.ResponseRegister
import retrofit2.Response

class IdentityRepository (
    private val apiService: ApiService,
) {
    suspend fun registerUser(registerRequestBody: RegisterRequest) : Response<ResponseRegister> {
        return apiService.registerUser(registerRequestBody)
    }

    suspend fun loginUser(loginUserRequestBody: LoginRequest) : Response<ResponseLogin> {
        return apiService.loginUser(loginUserRequestBody)
    }
}
package com.c23_pr505.batikco.remote

import com.c23_pr505.batikco.RGBByIdResponse
import com.c23_pr505.batikco.response.login.LoginRequest
import com.c23_pr505.batikco.response.login.ResponseLogin
import com.c23_pr505.batikco.response.register.RegisterRequest
import com.c23_pr505.batikco.response.register.ResponseRegister
import retrofit2.Response
import retrofit2.http.*

interface ApiService {

    @Headers("Accept: application/json")
    @POST("register")
    suspend fun registerUser(
        @Body body: RegisterRequest
    ): Response<ResponseRegister>

    @Headers("Accept: application/json")
    @POST("login")
    suspend fun loginUser(
        @Body body: LoginRequest
    ): Response<ResponseLogin>



}
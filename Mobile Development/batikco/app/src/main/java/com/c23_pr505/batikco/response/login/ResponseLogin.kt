package com.c23_pr505.batikco.response.login

import com.c23_pr505.batikco.response.Errors
import com.google.gson.annotations.SerializedName

data class LoginRequest (

    @field:SerializedName("password")
    val password: String,

    @field:SerializedName("email")
    val email: String
)

data class ResponseLogin(
    val errors: Errors,
    val message: String,
    val token: String
)
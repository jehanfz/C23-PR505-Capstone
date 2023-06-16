package com.c23_pr505.batikco.request

data class RegisterRequestBody (
    val name: String,
    val email: String,
    val password: String,
)
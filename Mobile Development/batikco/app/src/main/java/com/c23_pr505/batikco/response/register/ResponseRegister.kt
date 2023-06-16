package com.c23_pr505.batikco.response.register

import com.c23_pr505.batikco.response.Errors
import com.google.gson.annotations.SerializedName

data class RegisterRequest(

	@field:SerializedName("password")
	val password: String,

	@field:SerializedName("email")
	val email: String,

	@field:SerializedName("username")
	val username: String
)
data class ResponseRegister(
	val errors: Errors,
	val message: String
)

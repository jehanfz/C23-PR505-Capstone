package com.c23_pr505.batikco

import android.content.Context
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import androidx.core.splashscreen.SplashScreen.Companion.installSplashScreen
import com.c23_pr505.batikco.databinding.ActivityMainBinding
import com.c23_pr505.batikco.response.login.LoginRequest
import com.c23_pr505.batikco.viewmodel.AuthViewModel
import org.koin.androidx.viewmodel.ext.android.viewModel

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding
    private val authViewModel: AuthViewModel by viewModel()

    override fun onCreate(savedInstanceState: Bundle?) {
        installSplashScreen()
        super.onCreate(savedInstanceState)

        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.btnAmbilGambar.setOnClickListener {
            startActivity(Intent(this, CameraActivity::class.java))
        }

//        binding.btnHasil.setOnClickListener {
//            startActivity(Intent(this, HistoryActivity::class.java))
//        }

        binding.toolbarIcon.setOnClickListener {
            clearSharedPreferences()
        }

        checkSession()
    }

    private fun checkSession() {
        val sharedPref = getSharedPreferences("credentials", Context.MODE_PRIVATE)
        val email = sharedPref.getString("email", null)
        val password = sharedPref.getString("password", null)

        if (!email.isNullOrEmpty() && !password.isNullOrEmpty()) {
            authViewModel.loginUser(LoginRequest(email, password))
        } else {
            startActivity(Intent(this, LoginActivity::class.java))
        }
    }

    private fun clearSharedPreferences() {
        val sharedPref = getSharedPreferences("credentials", Context.MODE_PRIVATE)
        with(sharedPref.edit()) {
            clear()
            apply()
        }
        Toast.makeText(this, "Log out successful", Toast.LENGTH_SHORT).show()
        startActivity(Intent(this, LoginActivity::class.java))
    }
}
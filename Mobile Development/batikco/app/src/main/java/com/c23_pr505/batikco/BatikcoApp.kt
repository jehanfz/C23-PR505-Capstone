package com.c23_pr505.batikco

import android.app.Application
import android.content.Context
import com.c23_pr505.batikco.remote.ApiService
import com.c23_pr505.batikco.remote.RetrofitClient
import com.c23_pr505.batikco.repository.IdentityRepository
import com.c23_pr505.batikco.viewmodel.AuthViewModel
import org.koin.android.ext.koin.androidContext
import org.koin.android.ext.koin.androidLogger
import org.koin.androidx.viewmodel.dsl.viewModel
import org.koin.core.context.startKoin
import org.koin.dsl.module

class BatikcoApp : Application() {

    override fun onCreate() {
        super.onCreate()

        context = applicationContext

        startKoin {
            androidLogger()
            androidContext(this@BatikcoApp)
            modules(vmModule, repositoryModule)
        }
    }

    private val vmModule = module {
        viewModel { AuthViewModel(get()) }
    }

    private val repositoryModule = module {
        single { RetrofitClient.createService<ApiService>() }
        single { IdentityRepository(get()) }
    }

    companion object {
        lateinit var context: Context
    }
}
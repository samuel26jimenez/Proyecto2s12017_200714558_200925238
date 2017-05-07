package com.example.samuel.calendar_driver;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class Login extends AppCompatActivity {

    String user = "";
    String pass = "";
    EditText txtuser, txtpass;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        txtuser = (EditText) findViewById(R.id.editText);
        txtpass = (EditText) findViewById(R.id.editText2);
        Button login = (Button) findViewById(R.id.button);


        login.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View v){
                user = txtuser.getText().toString();
                pass = txtpass.getText().toString();
            }
        });


    }
}

package rafaelmorales.practica.com.drive_calendar;

import android.app.ProgressDialog;
import android.content.DialogInterface;
import android.content.Intent;
import android.os.AsyncTask;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.URL;

public class logInDrive extends AppCompatActivity {
    ProgressDialog cuadroDeDialogo;
    public String respuesta="", usuario="", contraseña="";
    TextView user, pass;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_log_in_drive);

        Button registro = (Button)findViewById(R.id.btnRegistro);
        Button inicio = (Button)findViewById(R.id.btnLogIn);
        user = (TextView)findViewById(R.id.txtUser);
        pass = (TextView)findViewById(R.id.txtPass);

        registro.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                usuario = user.getText().toString();
                contraseña = pass.getText().toString();
                AsyncCallWSRes2 conectarMetodo2 = new AsyncCallWSRes2();
                conectarMetodo2.execute();
            }
        });

        inicio.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                usuario = user.getText().toString();
                contraseña = pass.getText().toString();
                AsyncCallWSRes conectarMetodo2 = new AsyncCallWSRes();
                conectarMetodo2.execute();
            }
        });
    }

    private class AsyncCallWSRes extends AsyncTask<Void, Void, Void> {

        @Override
        protected Void doInBackground(Void... params) {
            Log.i("Vik", "doInBackground");

            Coneccion_API2();

            return null;
        }

        @Override
        protected void onPostExecute(Void result) {
            Log.i("Vik", "onPostExecute");
            cuadroDeDialogo.dismiss();
        }


        @Override
        protected void onPreExecute() {
            Log.i("Vik", "onPreExecute");
            super.onPreExecute();
            cuadroDeDialogo = new ProgressDialog(logInDrive.this);
            cuadroDeDialogo.setMessage("Cargando...");
            cuadroDeDialogo.setIndeterminate(false);
            cuadroDeDialogo.setProgressStyle(ProgressDialog.STYLE_SPINNER);
            cuadroDeDialogo.setCancelable(true);
            cuadroDeDialogo.show();
        }

        @Override
        protected void onProgressUpdate(Void... values) {
            Log.i("Vik", "onProgressUpdate");
        }
    }

    private class AsyncCallWSRes2 extends AsyncTask<Void, Void, Void> {

        @Override
        protected Void doInBackground(Void... params) {
            Log.i("Vik", "doInBackground");

            Coneccion_Registro();

            return null;
        }

        @Override
        protected void onPostExecute(Void result) {
            Log.i("Vik", "onPostExecute");
            cuadroDeDialogo.dismiss();
        }


        @Override
        protected void onPreExecute() {
            Log.i("Vik", "onPreExecute");
            super.onPreExecute();
            cuadroDeDialogo = new ProgressDialog(logInDrive.this);
            cuadroDeDialogo.setMessage("Cargando...");
            cuadroDeDialogo.setIndeterminate(false);
            cuadroDeDialogo.setProgressStyle(ProgressDialog.STYLE_SPINNER);
            cuadroDeDialogo.setCancelable(true);
            cuadroDeDialogo.show();
        }

        @Override
        protected void onProgressUpdate(Void... values) {
            Log.i("Vik", "onProgressUpdate");
        }
    }

    public void Coneccion_API2(){// VER SI EXISTE
        try {
            String cadena = "";
            URL url = new URL("http://192.168.43.122:58402/api/btree?activos="+cadena);
            HttpURLConnection coneccion = (HttpURLConnection) url.openConnection();
            coneccion.setRequestMethod("GET");
            coneccion.connect();

            InputStream input = coneccion.getInputStream();
            int byt;

            while((byt = input.read()) != -1){
                respuesta += (char) byt;
            }

            if (respuesta == "True"){
                Intent intent = new Intent(logInDrive.this, logInDrive.class);
                startActivity(intent);

            }else{
                AlertDialog.Builder build = new AlertDialog.Builder(logInDrive.this);
                build.setMessage("Información Incorrecta")
                        .setTitle("¡ ATENCION !")
                        .setCancelable(false)
                        .setNeutralButton("Aceptar", new DialogInterface.OnClickListener(){

                            @Override
                            public void onClick(DialogInterface dialog, int which) {
                                dialog.cancel();
                            }
                        });
                AlertDialog alerta = build.create();
                alerta.show();
            }

            //Log.d("json api", respuesta);

        }catch (Exception e){

        }
    }

    public void Coneccion_Registro(){//ALMACENAR
        try {
            String cadena = "";
            URL url = new URL("http://192.168.43.122:58402/api/btree?activos="+cadena);
            HttpURLConnection coneccion = (HttpURLConnection) url.openConnection();
            coneccion.setRequestMethod("GET");
            coneccion.connect();

            InputStream input = coneccion.getInputStream();
            int byt;

            while((byt = input.read()) != -1){
                respuesta += (char) byt;
            }

            if (respuesta == "True"){
                Intent intent = new Intent(logInDrive.this, Drive.class);
                startActivity(intent);

            }else{
                AlertDialog.Builder build = new AlertDialog.Builder(logInDrive.this);
                build.setMessage("Información Incorrecta")
                        .setTitle("¡ ATENCION !")
                        .setCancelable(false)
                        .setNeutralButton("Aceptar", new DialogInterface.OnClickListener(){

                            @Override
                            public void onClick(DialogInterface dialog, int which) {
                                dialog.cancel();
                            }
                        });
                AlertDialog alerta = build.create();
                alerta.show();
            }

            //Log.d("json api", respuesta);

        }catch (Exception e){

        }
    }
}

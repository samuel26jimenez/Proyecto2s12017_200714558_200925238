package rafaelmorales.practica.com.drive_calendar;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Button drive = (Button)findViewById(R.id.btn_drive);
        Button calendar = (Button)findViewById(R.id.btn_calendar);

        drive.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(MainActivity.this, logInDrive.class);
                startActivity(intent);
            }
        });

        calendar.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(MainActivity.this, logInCalendar.class);
                startActivity(intent);
            }
        });

    }
}

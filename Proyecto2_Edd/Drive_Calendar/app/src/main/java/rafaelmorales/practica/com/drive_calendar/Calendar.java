package rafaelmorales.practica.com.drive_calendar;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.CalendarView;

public class Calendar extends AppCompatActivity {
    CalendarView calender;
    Button boton, salir;
    public static String fecha;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_calendar);

        calender = (CalendarView)findViewById(R.id.calendarView);
        boton = (Button)findViewById(R.id.btnSeguir);
        salir = (Button)findViewById(R.id.btnSalir);

        calender.setOnDateChangeListener(new CalendarView.OnDateChangeListener() {

            @Override
            public void onSelectedDayChange(CalendarView view, int year, int month, int dayOfMonth) {
                // TODO Auto-generated method stub
                fecha = dayOfMonth +"/" + (month+1) + "/" + year;
            }
        });

        boton.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(Calendar.this, EventoCalendar.class);
                startActivity(intent);
            }
        });

        salir.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(Calendar.this, MainActivity.class);
                startActivity(intent);
            }
        });

    }
}

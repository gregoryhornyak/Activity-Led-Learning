// worldGen.h
// Written by Jozsef Hornyak
// Modified by Leo Head
// The world generation class

#ifndef WORLD_GENERATOR_H
#define WORLD_GENERATOR_H

#include <fstream>
#include <math.h>
#include <stdlib.h>
#include <string>
#include <iostream>
#include "../tools/pytag_converter.h"
#include "../interface/gameInterface.h"

class Island
{
public:

    ///BASIC SETTINGS: ---------------------------------------

        /// setters:
    std::string islandSeed = "";
    int mapSize_set = 100*100; ///1D array
    int numberOfIslets_set = 70;
    int border_set = 10;
    int isletSize_set = 5+1; /// x*2+1 -> square in which land spawns
    int numOfTrees_set = 10;
    int printRange_set = 20; ///x*2 -> printing screen size
    int steps_set = 4; ///navigation speed
        /// automatic
    int width = sqrt(mapSize_set);
        /// grids:
    std::string* mapGrid=new std::string[1]; ///grid for map
    int* islet_coordinates = new int[1]; /// list for islets
    int* NWSE_coast_coordinates= new int[1]; /// list for the right side coast
    int* abutment_coordinates = new int[20]; /// list for abutments
        /// sizes:
    int islet_coordinates_size = numberOfIslets_set*2;
    int mapGrid_size = mapSize_set;
    int NWSE_coast_coordinates_size = 0;


    ///CORE SETTINGS end ------------------------------------

    /**
        1. create mapGrid
        2. create islandsCoords
        3. create islet origins
        4. create islets
        5. cleaning + filling
        6. island size determination
        7. beach creation
        8. refining beaches
        9. side coast detector (NWSE)
        10. longest abutment counter
        + square lake removal
        + tree spawner
        + floodfill variants as:
          - lake_detector
          - lake_detector_all
          - area detector
        11. printer
        12. exporter to .txt
        + help for user
    */


    /**NEED:
    !!!
    -error checking: extremeties (lowest/highest)
        etc.
    !!!
    -list for lakes - 1. counts lakes 2. sizes into a list
        1. var for lake_count
        2. list for lake sizes - lake_count long
        3. go through lakes again, now store sizes
    -list of lands/islands - same as with lakes
    -abutment counter/finder doesnt work
        fix needed: counting after 3 found abuts
    */

        /// every export is indentical
/*
    time_t now01 = time(0);
    now01 -= 1609403226 - 2686619; /// 01 February
    string currentDate = to_string(now01);
*/

        /// basic variables:
    int mapSize = mapSize_set; /// control size of the map
    int numberOfIslands=numberOfIslets_set; /// number of islands -> they will merge into one
    int border = border_set; /// border that limits the islands spawning area
    ///regulation: isletSize must be dependent to borders!!!
    int isletSize = isletSize_set;
    int printRange = printRange_set;
    int steps = steps_set;
        ///later use
    int whichSide_lenght =0;
    int currentLake_size=0;

    /// random coordinates for the islands
    int randX = 0;
    int randY = 0;

    ///find borders:
    int minX=mapSize;
    int minY = mapSize;
    int maxX = 0;
    int maxY = 0;

    int spawnNew = 0;

        /// counters:
    int cleaning_counter = 0;
    int gap_counter = 0;
    int land_counter = 0;
    int beach_destroy_counter=0;
    int abutment_counter = 0;
    int abutment_counter_temp = 0;
    int tree_spawn_fail_counter = 0;

        ///booleans:
    bool does_exit = false;
    bool does_connect = false; /// false = disconnect / true = connect
    bool suitable4Tree;
    bool developer_mode=false;
    bool is_square_lake = true;
    bool cst_det_dir_VERTICAL = false;
    bool abuts_been_checked=false;

        ///sums:
    int numOfBeaches = 0;
    int numOfTrees = numOfTrees_set;
    int numOfLakes=0;
    int abutment_coordinates_size=20;
    float land_value = 0;
    float beach_value = 0;
    float world_value = 0;


        /// uncategorized
    int k2 = 0; /// beach finder hook
    int width_where=0;  /// printing counter
    int iT; /// tree place y
    int jT; /// tree place x
        /// automatic
    int posX = width/2; ///camera pos x
    int posY = width/2; ///camera pos y

    std::string direction; ///camera direction
    std::string space_char = " "; /// comes after tile - empty if thin map

    int for_start=0; ///from where to start
    int for_end=0;  ///when to stop
    int cardDirection = -1; /// 1 = left --> right / -1 = left <-- right
    int cardDirectionP_abut = 1; ///which side
    int smooth=0;


    /**----------------------------------------------------------------*/
        ///TILES
    std::string watr_00 = "1";   ///water - basic
    std::string watr_01 = "11";   ///water - ocean
    std::string watr_02 = "12"; ///water - lake

    std::string land_10 = "2";  ///land - plain
    std::string land_11 = "21";  ///land - ice
    std::string land_12 = "22";  ///land - rock
    std::string land_13 = "23";  ///land - desert

    std::string bech_2 = "3";  ///beach
    std::string cstl_3 = "4";   ///coastline
    std::string trot_4 = "5";   ///trunk of tree
    std::string fgot_5 = "6";   ///foliage of tree
    std::string pilr_6 = "7";   ///pillar [D] of bridge
    std::string abut_7 = "8";   ///abutment = real bridge start

    std::string isor_9 = "9"; /// origin of each islet


        ///Methods:

    Island(bool _dev , std::string _seed, int _mapSize, int _numOfIslets, int _border, int _isletSize, int _numOfTrees)
    {
        if(_dev == true)
        {
            developer_mode = true;
        }


        if(negative_Error(_border) == true)
        {
            std::cout<<"error with border set";
        }

        mapSize = pow(_mapSize,2);
        mapGrid_size = mapSize;

        mapGrid = new std::string[mapGrid_size];

        islet_coordinates_size = _numOfIslets;
        islet_coordinates=new int[islet_coordinates_size];

        border = _border;
        isletSize = _isletSize;
        numOfTrees = _numOfTrees;
        islandSeed = _seed;
        width = sqrt(mapSize);
        NWSE_coast_coordinates_size = width;
        NWSE_coast_coordinates = new int[NWSE_coast_coordinates_size];

        posX = width/2;
        posY = width/2;

        smooth = 1.5;

        std::cout << "Parameters successfully read." << std::endl;

            ///complete island creation
        mapGrid_creation();
        islandsCoords_creation();
        islet_origin_creation();
        islet_creation();
        cleaning_filling();
        beach_creation();
        beach_refinement();
        island_size_det();

        coast_detector("s");

        /// counter + coordNew + counter + abutPrint
        longst_abut_counter("s");
        abut_coord_new();
        longst_abut_counter("s");
        abut_printer();
        lake_2x2_remove();
        tree_spawner(200);

        std::cout << "\nAll methods done!\n" << std::endl;
        system("pause");

    }

    ~Island()
    {

        delete [] islet_coordinates;
        std::cout << "islets deleted" << ", ";
        delete [] mapGrid;
        std::cout << "mapGrid deleted" << ", ";
        delete [] NWSE_coast_coordinates;
        std::cout << "coastCoords deleted" << ", ";
        delete [] abutment_coordinates;
        std::cout << "abuts deleted" << std::endl;

        std::cout << std::endl << "Island class has been deleted" << std::endl;
    }

    void mapGrid_creation()
    {

            ///world map GRID creation
        for(int i = 0; i<mapSize; i++)
        {
            mapGrid[i] = watr_00; /// everything is water first
        }

        std::cout << "MapGrid ok" << std::endl;
    }

    void islandsCoords_creation()
    {

            ///islet coordinates creation
        for(int i = 0; i<islet_coordinates_size; i++)
        {
            islet_coordinates[i] = 0;
        }

        std::cout << "isletCoords ok" << std::endl;
    }

    void islet_origin_creation()
    {

            ///islets creation
        for(int i = 0; i<islet_coordinates_size; i++)
        {
            ///rand() % 30 + 1985;   range 1985-2014
            randX = rand() % (width-border*2) + border;
            randY = rand() % (width-border*2) + border;
            islet_coordinates[i] = xy_to_i( randX,randY, width) ;
            mapGrid[xy_to_i(randX,randY,width) ] = land_10;
            mapGrid[xy_to_i(randX,randY,width) ] = land_10;

        }

        std::cout << "isletO_creation ok" << std::endl;

    }

    void islet_creation()
    {

        if(isletSize > (border)-2)
        {
            isletSize = (border -2) ;
        }

        ///island spawning:

        for(int k=0; k<islet_coordinates_size; k++)
        {
            for(int i= -(isletSize-1); i<isletSize; i++)
            {
                for(int j= -(isletSize-1); j<isletSize; j++)
                {
                    if(i==0 && j==0)
                    {
                        continue;
                        ///mapGrid[ xy_to_i((islet_coordinates[xy_to_i(0,k,2)]),(islet_coordinates[xy_to_i(1,k,2)]),width) ]  = land_10;

                    }
                    spawnNew = rand() % (pythagorean(j,i)) ;
                    if(spawnNew == 0)
                    {
                        mapGrid[ islet_coordinates[k] + xy_to_i(j,i, width) ]  = land_10;
                    }
                }
            }
        }
        std::cout << "islets_creation ok - with isletSize: " << isletSize << std::endl;
    }

    void cleaning_filling()
    {

        ///cleaning for 'k' times
        ///+filling for 'k' times

        for(int k =0; k<11; k++) /// bigger k means much more detended coastline
        {
            for(int i = width+1; i<mapSize-1-width; i++)
            {
                if(i_to_xy(i,0,width) == 1 || i_to_xy(i,0,width) == mapSize-1)
                {
                    continue;
                }
                ///land replace
                if(mapGrid[i] == land_10)
                {
                    for(int a=-1; a<2; a++)
                    {
                        for(int b=-1; b<2; b++)
                        {
                            if(a==0 && b==0)
                            {
                                continue;
                            }
                            if(mapGrid[ i + xy_to_i(b,a,width) ] == watr_00)
                            {
                                cleaning_counter++;
                            }
                        }
                    }
                }
                ///water replace
                if(mapGrid[i] == watr_00)
                {
                    for(int a=-1; a<2; a++)
                    {
                        for(int b=-1; b<2; b++)
                        {
                            if(a==0 && b==0)
                            {
                                continue;
                            }
                            if(mapGrid[ i + xy_to_i(b,a,width) ] == land_10)
                            {
                                gap_counter++;
                            }
                        }
                    }
                }
                ///land replacement
                if(cleaning_counter > 5)
                {
                    mapGrid[i] = watr_00;
                }
                ///reset counter
                cleaning_counter = 0;
                ///water replacement
                if(gap_counter > 5)
                {
                    mapGrid[i] = land_10;
                }
                ///reset counter
                gap_counter = 0;
            }
        }

        std::cout << "clean+fill ok" << std::endl;
    }

    void island_size_det()
    {
            /// size determination
        for(int i=0; i<mapSize; i++)
        {
            if(mapGrid[i] == land_10)
            {
                if(i_to_xy(i,0,width) < minX)
                {
                    minX = i_to_xy(i,0,width);
                }
                if(i_to_xy(i,0,width) > maxX)
                {
                    maxX = i_to_xy(i,0,width);
                }

                if(i_to_xy(i,1,width) < minY)
                {
                    minY = i_to_xy(i,1,width);
                }
                if(i_to_xy(i,1,width) > maxY)
                {
                    maxY = i_to_xy(i,1,width);
                }
            }
        }
            ///why plus?
/*
        minX++;
        minY++;
        maxX++;
        maxY++;
        */

        std::cout << "islandSizeDet ok" << std::endl;
    }

    void beach_creation()
    {

        ///beach creation = border of island
        ///1 block wide beach

        for(int i=1+width; i<mapSize-1-width; i++)
        {
            if(i_to_xy(i,0,width) == 1 || i_to_xy(i,0,width) == mapSize-1)
            {
                continue;
            }

            if(mapGrid[i] == land_10)
            {
                for(int a=-1; a<2; a++)
                {
                    if(does_exit == true)
                    {
                        break;
                    }

                    for(int b=-1; b<2; b++)
                    {
                        if(does_exit == true)
                        {
                            break;
                        }

                        if(a==0 && b==0)
                        {
                            continue;
                        }

                        if(mapGrid[ i + xy_to_i(b,a,width) ] == watr_00)
                        {
                            does_exit = true;
                        }
                    }
                }
            }

            if(does_exit == true)
            {
                ///numOfBeaches++; now in printer
                mapGrid[i] = bech_2;
            }

            does_exit = false;
        }

        std::cout << "BeachCreation ok" << std::endl;
    }

    void beach_refinement()
    {

        ///refining beaches

        for(int i=1; i<mapSize-1; i++)
        {
            if(i_to_xy(i,0,width) == 1 || i_to_xy(i,0,width) == mapSize-1)
            {
                continue;
            }

            if(mapGrid[i] == bech_2)
            {
                for(int a=-1; a<2; a++)
                {
                    for(int b=-1; b<2; b++)
                    {
                        if(a==0 && b==0)
                        {
                            continue;
                        }
                        if(mapGrid[ i + xy_to_i(b,a,width) ] != land_10)
                        {
                            beach_destroy_counter++;
                        }
                    }
                }
            }

            if(beach_destroy_counter == 8)
            {
                mapGrid[i] = watr_00;
                ///numOfBeaches--;
            }

            beach_destroy_counter=0;
        }

        std::cout << "beachRef ok" << std::endl;
    }

    void coast_detector(std::string _cardinal) /// N/W/S/E
    {

    //abutment_coordinates = new int[abutment_coordinates_size];

    /// settings based on input:

        if(_cardinal == "N" || _cardinal == "n")
        {
            for_start = minY;
            for_end = maxY-1;
            cardDirection = 1;
            whichSide_lenght=maxX-minX;
            NWSE_coast_coordinates = new int[whichSide_lenght];
            cst_det_dir_VERTICAL=1;
        }
        else if(_cardinal == "S" || _cardinal == "s")
        {
            for_start = maxY;
            for_end = minY+1;
            cardDirection=-1;
            whichSide_lenght=maxX-minX;
            NWSE_coast_coordinates = new int[whichSide_lenght];
            cst_det_dir_VERTICAL=1;
        }
        else if(_cardinal == "E" || _cardinal == "e")
        {
            for_start = maxX;
            for_end = minX+1;
            cardDirection = -1;
            whichSide_lenght = maxY-minY;
            NWSE_coast_coordinates = new int[whichSide_lenght];
            cst_det_dir_VERTICAL=0;
        }
        else if(_cardinal == "W" || _cardinal == "w")
        {
            for_start = minX;
            for_end = maxX-1;
            cardDirection = 1;
            whichSide_lenght = maxY-minY;
            NWSE_coast_coordinates = new int[whichSide_lenght];
            cst_det_dir_VERTICAL=0;
        }


        /// coast detector:

            /// vertical
        if(cst_det_dir_VERTICAL==0)
        {
            for(int k=minY; k<whichSide_lenght+minY; k++) ///doesn't change
            {
                for(int j = for_start; j!=for_end; j= j+cardDirection) ///changes
                {
                    if(mapGrid[ xy_to_i(j,k,width) ] == bech_2)
                    {
                        NWSE_coast_coordinates[k-minY] = xy_to_i(j,k,width);
                        //mapGrid[ xy_to_i( (j - cardDirection) ,k,width) ] = cstl_3;
                        break;
                    }
                }
            }
        }
        else if(cst_det_dir_VERTICAL==1)
        {
            for(int k=minX; k<whichSide_lenght+minX; k++) ///doesn't change
            {
                for(int j = for_start; j!=for_end; j= j+cardDirection) ///changes
                {
                    if(mapGrid[ xy_to_i(k,j,width) ] == bech_2)
                    {
                        NWSE_coast_coordinates[k-minX] = xy_to_i(k,j,width);
                        //mapGrid[ xy_to_i(k,(j - cardDirection),width) ] = cstl_3;
                        break;
                    }
                }
            }
        }

        std::cout << "coastDet ok" << std::endl;
    }

    void longst_abut_counter(std::string _cardinalP) /// NWSE
    {
        if(_cardinalP == "E" || _cardinalP == "e")
        {
            cardDirectionP_abut = 1;
        }
        else if(_cardinalP == "W" || _cardinalP == "w")
        {
            cardDirectionP_abut = -1;
        }
                /// abut counter
               ///vertical
              ///right side

        for(int i=3*width; i<mapSize-3*width; i++)
        {
            if(i_to_xy(i,0,width) < 3 || i_to_xy(i,0,width) > width-3)
            {
                continue;
            }
            /// checking part:
                //cout<<"a"<<" ";
            if(   mapGrid[i] == bech_2
               && mapGrid[i- xy_to_i(0,1,width) ] == bech_2
               && mapGrid[i+ xy_to_i(0,1,width)] == bech_2
               && mapGrid[i+cardDirectionP_abut] == watr_00
               )
            {
                //cout<<"B"<<" ";
                if(abuts_been_checked = 1)
                {
                    abutment_coordinates[0] = i;
                }

                abutment_counter = 1;
                k2=i+ xy_to_i(0,0,width) ;
                while(mapGrid[k2] == bech_2 && mapGrid[k2+cardDirectionP_abut] == watr_00)
                {
                    //cout<<"C"<<" ";
                    abutment_counter++;
                    k2+=width;
                    if(abuts_been_checked = 1)
                    {
                        abutment_coordinates[abutment_counter-1 ] = k2;
                    }
                    if(abuts_been_checked = 1 && abutment_counter == abutment_coordinates_size)
                    {
                        break;
                    }
                    ///problem: no abutmax

                }
            }

            if(abutment_counter > abutment_counter_temp)
            {
                abutment_counter_temp=abutment_counter;
            }
            if(abutment_counter == abutment_coordinates_size && abuts_been_checked == 1)
            {
                break;
            }
        }

        abuts_been_checked = true;

        std::cout << "longstAbutCount ok" << std::endl;
    }

    void abut_coord_new()
    {

        abutment_coordinates_size = abutment_counter_temp-2;
        std::cout << "abut_coord_size done with " << abutment_coordinates_size << " array size, ";
        abutment_coordinates = new int[abutment_coordinates_size];

        std::cout << "abutCoordsArray ok" << std::endl;

    }

    void abut_printer()
    {
        for(int i=0; i<abutment_coordinates_size; i++)
        {
            mapGrid[ abutment_coordinates[i] ] = abut_7;
        }

        std::cout << "longest abutment starting point: ";
        std::cout << "(" << i_to_xy(abutment_coordinates[0],0,width) << "," << i_to_xy(abutment_coordinates[0],1,width) << ")" << std::endl;

        std::cout << "abutPrint ok" << std::endl;
    }

    void island_origin_mark()
    {
        ///island-origin-finder
        if(developer_mode == true)
        {
            for(int k=0; k<islet_coordinates_size; k++)
            {
                mapGrid[ islet_coordinates[k] ] = isor_9;
            }
        }
        else
        {
            std::cout << "Developer mode is off" << std::endl;
        }
        std::cout << "islandOmarking ok" << std::endl;
    }

    void lake_2x2_remove()
    {
        for(int i=0+ width*5 ; i<mapSize- width*5 ; i++)
        {
            if( i_to_xy(i,0,width) < 5 || i_to_xy(i,0,width) > width-6 )
            {
                continue;
            }

            is_square_lake = true;
            if(mapGrid[i] == watr_00)
            {
                if(mapGrid[i+1] == watr_00
                && mapGrid[i+width] == watr_00
                && mapGrid[i+1+width] == watr_00)
                {
                    for(int a=-2; a<4; a++)
                    {
                        for(int b=-2; b<4; b++)
                        {
                            if( ( b==0 || b==1) && ( a==0 || a==1 ) )
                            {
                                continue;
                            }
                            if( mapGrid[ i + xy_to_i( b,a, width ) ] != bech_2
                               && mapGrid[ i + xy_to_i( b,a, width ) ] != land_10  )
                            {
                                is_square_lake = false;
                            }
                        }
                    }

                    if(is_square_lake == true)
                    {
                        for(int a=-1; a<3; a++)
                        {
                            for(int b=-1; b<3; b++)
                            {
                                mapGrid[i + xy_to_i( b,a, width ) ] = land_10;
                            }
                        }
                    }
                }
            }
        }
        std::cout << "2x2 lakes ok" << std::endl;
    }

    void tree_spawner(int _treeSum)
    {
        if(_treeSum != -1)
        {
            numOfTrees = _treeSum;
        }
            /// TREE SPAWNER >
        for(int k = 0; k<numOfTrees; k++)
        {
            tree_spawn_fail_counter = 0;
            while(true)
            {
                iT = rand() % (width-border*2);
                iT+= border;
                jT = rand() % (width-border*2);
                jT += border;

                if(mapGrid[ xy_to_i(jT,iT,width) ] == land_10 )
                {
                    break;
                }
                else
                {
                    tree_spawn_fail_counter++;
                }
                if(tree_spawn_fail_counter == 5)
                {
                    break;
                }
            }

            suitable4Tree = true;

            for(int i2 = -1-1; i2<2+1; i2++)
            {
                for(int j2 = -1-1; j2<2+1; j2++)
                {
                    if(mapGrid [ xy_to_i(jT+j2,iT+i2,width) ] != land_10)
                    {
                        suitable4Tree=false;
                    }
                }
            }
            /// end of search
            if(suitable4Tree==true)
            {
                mapGrid[xy_to_i(jT,iT,width)] = trot_4;
                mapGrid[xy_to_i(jT,iT-1,width)] = trot_4;
                mapGrid[xy_to_i(jT,iT-2,width)] = fgot_5;
                mapGrid[xy_to_i(jT-1,iT-2,width)] = fgot_5;
                mapGrid[xy_to_i(jT+1,iT-2,width)] = fgot_5;
                mapGrid[xy_to_i(jT,iT-3,width)] = fgot_5;
            }
        }
            /// TREE SPAWNER <
        std::cout << "treeSpawning ok" << std::endl;
    }

    void area_detector(int _x, int _y, std::string _target_tile, std::string _new_tile)
    {
        int x2 = _x;
        int y2 = _y;
        int i = xy_to_i(x2,y2, width);

        ///base cases:
        if(x2 < 0 || x2 > width-1 || y2 < 0 || y2 > width-1)
        {
            return;
        }
        if(mapGrid[i] != _target_tile )
        {
            return;
        }

        mapGrid[i] = _new_tile;

        lake_detector(x2+1, y2);
        lake_detector(x2-1, y2);
        lake_detector(x2, y2+1);
        lake_detector(x2, y2-1);

        std::cout << "areaDet ok" << std::endl;
    }

    void lake_detector(int _x, int _y)
    {
        int x2 = _x;
        int y2 = _y;
        int i = xy_to_i(x2,y2, width);

        ///base cases:
        if(x2 < 0 || x2 > width-1 || y2 < 0 || y2 > width-1)
        {
            return;
        }
        if(mapGrid[i] != watr_00 )
        {
            return;
        }

        mapGrid[i] = watr_01;

        lake_detector(x2+1, y2);
        lake_detector(x2-1, y2);
        lake_detector(x2, y2+1);
        lake_detector(x2, y2-1);

    }

    void lake_detector_all()
    {
        for(int i=0; i<mapGrid_size; i++)
        {
            if(mapGrid[i] == watr_00)
            {
                numOfLakes++;
                lake_detector(i_to_xy(i, 0, width), i_to_xy(i, 1, width) );
            }
        }
    }

    void current_lake_size()
    {
        //cout<<currentLake_size<<" blocks."<<endl;
        std::cout << std::endl << "Exactly " << numOfLakes << " lakes found." << std::endl;
    }

    void biome_generator()
    {
        /*
        string element_numbers = {1,2,3,4}
        string elements_list = {"D","R","I","P"}
        */

    }

    void legend_of_Island()
    {
        std::cout << "0 means water (blue)" << std::endl;
        std::cout << "1 means land (green)" << std::endl;
        std::cout << "2 means beach/coast (yellow)" << std::endl;
        std::cout << "3 means coastline (white)" << std::endl;
        std::cout << "4 means trunk of tree (brown)" << std::endl;
        std::cout << "5 means foliage of tree (green)" << std::endl;
        std::cout << "6 means pillar for bridge (white)" << std::endl;
        std::cout << "9 means islet origin point (x)" << std::endl;
    }

    void Printer(int _printRange, int _steps)
    {
        printRange = _printRange;
        steps = _steps;
        while(true)
        {
            for(int i = xy_to_i(posX-printRange,posY-printRange,width) ; i < xy_to_i(posX+printRange,posY+printRange,width) ; i++)
            {
                //for(int j = posX - printRange; j<posX+printRange; j++)

                if(width_where==printRange*2)
                {
                    std::cout << std::endl;
                    width_where=0;
                    i+=width-printRange*2;
                }
                width_where++;
                if(mapGrid[i] == watr_00) /// 0 means                                WATER
                {
                    std::cout << "\x1B[96m.\033[0m" << space_char;
                    ///cout<<"\033[3;106;96m.\033[0m"<<"";
                }
                else if(mapGrid[i] == watr_01) /// 0 means                                WATER
                {
                    ///cout<<"."<<" ";
                    std::cout << "\x1B[34m.\033[0m" << space_char;
                    ///cout<<"\033[3;106;96m.\033[0m"<<"";
                }

                else if(mapGrid[i]== land_10) /// 1 means                           LAND
                {
                    land_counter++;
                    ///cout<<"#"<<" ";
                    std::cout << "\x1B[32m#\033[0m" << space_char;
                }
                else if(mapGrid[i] == bech_2) /// 4 means beach from land =         BEACH
                {
                    numOfBeaches++;
                    ///cout<<"*"<<" ";
                    std::cout << "\x1B[93m*\033[0m" << space_char;
                }

                else if(mapGrid[i] == pilr_6) /// 5 means abutment = bridge start = PILLAR
                {
                    ///cout<<"*"<<" ";
                    std::cout << "\x1B[97mI\033[0m" << space_char;
                }

                else if(mapGrid[i] == abut_7) /// 5 means abutment = bridge start = PILLAR
                {
                    ///cout<<"*"<<" ";
                    std::cout << "\x1B[97mH\033[0m" << space_char;
                }

                else if(mapGrid[i] == cstl_3) /// 6 means pillar = bridge start =   COASTLINE
                {
                    ///cout<<"*"<<" ";
                    std::cout << "\x1B[97mI\033[0m" << space_char;
                }

                else if(mapGrid[i] == trot_4) /// 7 means trunk                     TREE
                {

                    ///cout<<"*"<<" ";
                    std::cout << "\033[3;100;90mH\033[0m" << space_char;
                }
                else if(mapGrid[i] == fgot_5) /// 8 means foliage                   TREE
                {
                    land_counter++;
                    ///cout<<"*"<<" ";
                    std::cout << "\033[3;42;32mO\033[0m" << space_char;
                }
                if(developer_mode == true)
                {
                    if(mapGrid[i] == "9")
                    {
                        std::cout << "X" << space_char;
                    }
                }
            }
            std::cout << posX << ", " << posY << std::endl;
            GameUI().uiPrinter();
            std::cout << "Type e to exit" << std::endl;
            std::cout << "Which direction? ";
            std::cin >> direction;
            if(direction == "a")
            {
                posX-=steps;
            }
            else if(direction == "d")
            {
                posX+=steps;
            }
            else if(direction == "w")
            {
                posY-=steps;
            }
            else if(direction == "s")
            {
                posY+=steps;
            }
            else if(direction == "e")
            {
                break;
            }

            if(posX-printRange <= 1)
            {
                posX+=steps;
            }
            if(posX+printRange >= mapSize-1)
            {
                posX-=steps;
            }
            if(posY-printRange <= 1)
            {
                posY+=steps;
            }
            if(posY+printRange >= mapSize-1)
            {
                posY-=steps;
            }
        }
    }



    void details_Island()
    {

        land_value = land_counter;
        beach_value = numOfBeaches;
        world_value = width*width;

        std::cout << "Island details:" << std::endl;
        std::cout << "  " << "Map size: " << width << "*" << width << std::endl;
        std::cout << "  " << "X width: " << minX << " - " << maxX << std::endl;
        std::cout << "  " << "Y width: " << minY << " - " << maxY << std::endl;
        std::cout << "  " << numOfBeaches << " beaches are there." << std::endl << std::endl;
        std::cout << "  " << "a " << abutment_coordinates_size << "-metre wide suitable abutment." << std::endl;
        std::cout << "  " << land_value << " tiles of land" << std::endl;
        std::cout << "  " << ( (land_value+beach_value) / (world_value) )*100 << "% is land, " << (land_value / (world_value))*100 << "% is livable." << std::endl;

        system("pause");
    }

    void Output_To_File(std::string Filename)
    {
        Filename = Filename + ".txt";;
        std::ofstream MyFile(Filename);

        MyFile << width << " " << numberOfIslands << " " << border << " " << isletSize << " " << std::endl;

        for(int i=0; i<mapSize; i++)
        {
            if(i%width == 0 && i!=0)
            {
                MyFile << std::endl;
            }
            if(mapGrid[i] == "01")
            {
                MyFile << "0" << " ";
            }
            else
            {
                MyFile << mapGrid[i] << " ";
            }

        }
        MyFile.close();
    }

    bool negative_Error(int integer)
    {
        if(integer < 0)
        {
            return 1;
        }
        else
        {
            return 0;
        }

    }

    void help()
    {
        std::cout << "When creating an island, you have to set: " << std::endl;
        std::cout << " whether you are an admin on not (0 is not, 1 is yes)" << std::endl;
        std::cout << " the seed for random island generation" << std::endl;
        std::cout << " the size of the map (as it is square sized, you only give the width)" << std::endl;
        std::cout << " the number of islets that will merge into one big (=density)" << std::endl;
        std::cout << " the border width (how much ocean surrounds the island)" << std::endl;
        std::cout << " the maximum size of each islet (much be less than the border)" << std::endl;
        std::cout << " and the number of trees that will spawn." << std::endl << std::endl;

        std::cout << "Existing methods list:" << std::endl;
        std::cout << " lake_2x2_remove (removes small lakes)" << std::endl;
        std::cout << " tree_spawner (requires number of trees, type '-1' for standard number)" << std::endl;
        std::cout << " printer (needs printing range and steps for scrolling)" << std::endl;
        std::cout << " output_to_file exports the map into a 2D .txt array with given name (type in filename)" << std::endl;
        //std::cout << " " << std::endl;
        std::cout << "!!!\nControls: 'wasd' for 4 directions, 'e' for exit\n!!!\n" << std::endl;
        system("pause");

             /**(bool admin, int _seed, int _mapSize, int _numOfIslets, int _border,
    /    int _isletSize, int _numOfTrees)*/

    }
};


#endif // WORLDGEN_H

clear all
%close all
clf
clc

% defining the grid size...
xx = 10; % 0 - 10 ...
yy = 10; % 0 - 10 ...

% Defining the obstacles...
obstacles(1,:)=[0,3];
obstacles(2,:)=[1,1];
obstacles(3,:)=[2,1];
obstacles(4,:)=[2,3];
obstacles(5,:)=[3,1];
obstacles(6,:)=[3,2];
obstacles(7,:)=[3,3];
obstacles(8,:)=[3,5];
obstacles(9,:)=[3,7];
obstacles(10,:)=[4,3];
obstacles(11,:)=[4,5];
obstacles(12,:)=[5,1];
obstacles(13,:)=[5,5];
obstacles(14,:)=[6,3];
obstacles(15,:)=[6,4];
obstacles(16,:)=[6,5];
obstacles(17,:)=[6,6];
obstacles(18,:)=[6,7];
obstacles(19,:)=[6,8];
obstacles(20,:)=[6,9];
obstacles(21,:)=[6,10];
obstacles(22,:)=[7,2];
obstacles(23,:)=[7,3];
obstacles(24,:)=[8,5];
obstacles(25,:)=[9,3];
obstacles(26,:)=[9,5];
obstacles(27,:)=[10,3];

% Defining starting and goal locations...
startingPosition=[5,7];
goal=[9,8];

% Define the colors of nodes...
obstacleColor=[1,0,0];  %red
nodeColor=[0,1,0];      %green
expandColor=[0,0,0];    %black
goalColor=[0,0,1];      %blue
pathColor=[0,1,1];      %cyan

% Plotting the grid and obstacles...
s = scatter(obstacles(:,1), obstacles(:,2), 150, ...
    obstacleColor, 'filled', 's', 'MarkerEdgeColor', 'b');
grid on;
% grid monor;
% grid(gca,'minor')
set(gca, 'YMinorTick','on', 'XMinorTick','on')
axis([0 10 0 10]);
hold on;

% Plotting the goal position...
scatter(goal(1,1), goal(1,2), 100, goalColor, 'filled');

% Initializing variables...
pathCount=1;  % Keeps track of the current node in the bfs_queue set...
tempCount=1;    % Keeps track of the end of the bfs_queue set...

% Initialize the bfs_queue set as ...
% bfs_queue(xPosition, yPosition, parentNode)...
bfs_queue(pathCount,:)=[startingPosition, pathCount];

%This loop executes until the goal is found...
while (~((bfs_queue(pathCount,1)==goal(1,1)) & ...
        (bfs_queue(pathCount,2)==goal(1,2))))
    
    % Plot the starting node (Source) ...
    scatter(bfs_queue(pathCount,1), bfs_queue(pathCount,2), ...
        100, nodeColor, 'filled');
    
    % Exploring the neighbour (left right top bottom)...
    for x=-1:1
        for y=-1:1
            % Ensuring the bfs_queue set does not expanded diagonally...
            if (x*y==0)
                
                % 'failsTest' is used to determine outside the grid, 
                % on an obstacle,
                % or it has already been expanded...
                failsTest=0;
                % 'tempNode' is the current node that is trying to 
                % be expanded...
                tempNode=[bfs_queue(pathCount,1)+x, ...
                    bfs_queue(pathCount,2)+y, pathCount];

                % Test if the node is outside grid...
                if ( (tempNode(1,1)<0) | (tempNode(1,2)<0) ) | ...
                        ( (tempNode(1,1)>xx) | (tempNode(1,2)>yy) )
                    failsTest=failsTest+1;
                end

                % Test to see if node is already in bfs_queue set...
                if (failsTest<1)
                    for i=1:size(bfs_queue,1)
                        if (tempNode(1,1)==bfs_queue(i,1)) & ...
                                (tempNode(1,2)==bfs_queue(i,2))
                            failsTest=failsTest+1;
                        end
                    end
                end

                % Test to see if node is an obstacle...
                if (failsTest < 1)
                    for i=1:size(obstacles,1)
                        if (tempNode(1,1)==obstacles(i,1)) & ...
                                (tempNode(1,2)==obstacles(i,2))
                            failsTest=failsTest+1;
                        end
                    end
                end

                % If not fail any tests, add to end of bfs_queue.
                % In BFS, nodes are removed from the end of the bfs_queue, 
                % so to make things easy, add new nodes to the end.
                if (failsTest < 1)
                    bfs_queue(pathCount+tempCount,:) = tempNode;
                    scatter(tempNode(1,1), tempNode(1,2), 120, ...
                        expandColor, 'filled');
                    tempCount=tempCount+1;
                end
            end
        end
    end
    
    % Increment to the next node...
    % Also decrement tempCount as it is a position in the bfs_queue...
    % Set relative to pathCount...
    pathCount=pathCount+1;
    tempCount=tempCount-1;
    pause(.1);
end

% Initialize a counter...
i=1;

% Trace back through the parent nodes to receover the path...
while ~(pathCount==1)
    path(i,:)=[bfs_queue(pathCount,1),bfs_queue(pathCount,2)];
    pathCount=bfs_queue(pathCount,3);
    i=i+1;
end

% Add the start position to the path...
path(i,:)=startingPosition;

% Plot the path...
plot(path(:,1),path(:,2));
scatter(path(:,1), path(:,2), 60, pathColor, ...
    'filled', 'MarkerEdgeColor', 'b');

